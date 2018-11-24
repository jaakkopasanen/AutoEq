# Denon AH-D5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 4.6; 31 3.4; 34 2.3; 37 1.6; 41 1.1; 45 0.8; 49 0.5; 54 0.4; 60 0.5; 66 0.5; 72 0.3; 79 0.2; 87 0.3; 96 0.3; 106 0.3; 116 0.3; 128 0.2; 141 0.1; 155 0.1; 170 0.2; 187 0.3; 206 0.5; 227 0.7; 249 0.9; 274 1.1; 302 1.3; 332 1.7; 365 2.0; 402 2.2; 442 2.6; 486 2.3; 535 1.7; 588 0.9; 647 -0.3; 712 -1.5; 783 -2.4; 861 -3.2; 947 -1.0; 1042 -0.9; 1146 -1.2; 1261 -0.6; 1387 -0.2; 1526 0.0; 1678 0.6; 1846 1.3; 2031 2.0; 2234 2.4; 2457 1.9; 2703 0.9; 2973 -0.2; 3270 -0.9; 3597 -1.4; 3957 -0.3; 4353 0.3; 4788 1.7; 5267 2.9; 5793 1.4; 6373 0.6; 7010 1.1; 7711 0.3; 8482 0.0; 9330 -2.5; 10263 -3.0; 11289 -2.0; 12418 -1.5; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -1.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.62 | 6.2 dB  |
| Peaking | 458 Hz   | 1.21 | 2.9 dB  |
| Peaking | 805 Hz   | 2.1  | -3.7 dB |
| Peaking | 2193 Hz  | 3.52 | 2.7 dB  |
| Peaking | 10258 Hz | 4.21 | -3.5 dB |
| Peaking | 39 Hz    | 1.88 | -0.4 dB |
| Peaking | 1171 Hz  | 9.45 | -0.6 dB |
| Peaking | 3530 Hz  | 4.01 | -1.9 dB |
| Peaking | 5249 Hz  | 3.21 | 2.8 dB  |
| Peaking | 12044 Hz | 8.05 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000/Denon%20AH-D5000.png)