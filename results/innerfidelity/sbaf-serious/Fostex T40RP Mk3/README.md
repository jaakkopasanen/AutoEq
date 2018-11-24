# Fostex T40RP Mk3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.3; 49 4.5; 54 3.6; 60 2.7; 66 2.0; 72 1.4; 79 0.8; 87 0.4; 96 0.1; 106 0.0; 116 -0.1; 128 -0.3; 141 -0.3; 155 -0.2; 170 0.1; 187 0.3; 206 0.6; 227 0.7; 249 0.7; 274 0.6; 302 0.2; 332 0.0; 365 0.6; 402 0.5; 442 1.5; 486 -0.0; 535 -0.6; 588 -0.8; 647 -0.7; 712 -1.2; 783 -1.1; 861 -0.5; 947 -0.4; 1042 0.2; 1146 0.3; 1261 1.3; 1387 1.2; 1526 1.3; 1678 1.1; 1846 0.6; 2031 1.3; 2234 1.5; 2457 1.5; 2703 1.8; 2973 1.5; 3270 0.8; 3597 -0.0; 3957 -1.5; 4353 -2.3; 4788 -1.0; 5267 3.7; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.4; 9330 -3.9; 10263 -1.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T40RP Mk3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T40RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.94 | 6.9 dB  |
| Peaking | 2708 Hz | 1.12 | 2.0 dB  |
| Peaking | 4451 Hz | 2.64 | -5.6 dB |
| Peaking | 5813 Hz | 2.57 | 7.8 dB  |
| Peaking | 9296 Hz | 4.27 | -4.9 dB |
| Peaking | 49 Hz   | 2.84 | 1.3 dB  |
| Peaking | 116 Hz  | 1    | -1.3 dB |
| Peaking | 297 Hz  | 0.51 | 0.9 dB  |
| Peaking | 706 Hz  | 1.67 | -1.7 dB |
| Peaking | 1349 Hz | 4.16 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T40RP%20Mk3/Fostex%20T40RP%20Mk3.png)