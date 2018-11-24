# Plane Quiet Platinum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.7; 25 -2.1; 28 -3.1; 31 -3.4; 34 -3.2; 37 -2.8; 41 -2.3; 45 -1.9; 49 -1.5; 54 -1.3; 60 -1.2; 66 -1.0; 72 -0.7; 79 -0.5; 87 -0.4; 96 -0.4; 106 -0.5; 116 -0.7; 128 -0.8; 141 -0.7; 155 -0.6; 170 -0.5; 187 -0.2; 206 0.0; 227 -0.1; 249 0.2; 274 1.1; 302 1.5; 332 2.0; 365 2.5; 402 2.8; 442 3.1; 486 3.4; 535 3.6; 588 3.4; 647 3.1; 712 2.5; 783 2.1; 861 2.1; 947 1.0; 1042 1.2; 1146 1.1; 1261 0.6; 1387 0.7; 1526 3.1; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plane Quiet Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plane Quiet Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 1.57 | -3.4 dB |
| Peaking | 148 Hz   | 1.22 | -0.9 dB |
| Peaking | 486 Hz   | 1.29 | 3.6 dB  |
| Peaking | 2338 Hz  | 1.24 | 5.9 dB  |
| Peaking | 4946 Hz  | 1.55 | 5.6 dB  |
| Peaking | 1400 Hz  | 3.19 | -2.7 dB |
| Peaking | 1661 Hz  | 5.12 | 3.4 dB  |
| Peaking | 6482 Hz  | 4.58 | 3.5 dB  |
| Peaking | 7412 Hz  | 2.07 | -2.3 dB |
| Peaking | 11071 Hz | 1.26 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Plane%20Quiet%20Platinum/Plane%20Quiet%20Platinum.png)