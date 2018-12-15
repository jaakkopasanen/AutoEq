# Plane Quiet Platinum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -1.0; 25 -2.3; 28 -3.3; 31 -3.4; 34 -3.1; 37 -2.7; 41 -2.1; 45 -1.6; 49 -1.2; 54 -0.9; 60 -0.9; 66 -0.8; 72 -0.7; 79 -0.7; 87 -0.7; 96 -0.8; 106 -1.0; 116 -1.2; 128 -1.3; 141 -1.3; 155 -1.2; 170 -1.1; 187 -0.7; 206 -0.5; 227 -0.5; 249 -0.3; 274 0.4; 302 0.7; 332 1.1; 365 1.5; 402 1.8; 442 2.0; 486 2.2; 535 2.4; 588 2.3; 647 2.1; 712 1.6; 783 1.6; 861 1.9; 947 1.0; 1042 1.1; 1146 0.9; 1261 0.3; 1387 0.7; 1526 3.5; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plane Quiet Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plane Quiet Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 1.87 | -3.5 dB |
| Peaking | 137 Hz  | 1.18 | -1.3 dB |
| Peaking | 223 Hz  | 2.52 | -0.2 dB |
| Peaking | 476 Hz  | 1.52 | 2.2 dB  |
| Peaking | 3239 Hz | 0.66 | 6.9 dB  |
| Peaking | 1371 Hz | 2.99 | -4.5 dB |
| Peaking | 1648 Hz | 2.49 | 4.2 dB  |
| Peaking | 3204 Hz | 2.27 | -1.2 dB |
| Peaking | 6230 Hz | 2.08 | 5.8 dB  |
| Peaking | 7420 Hz | 1.44 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plane%20Quiet%20Platinum/Plane%20Quiet%20Platinum.png)