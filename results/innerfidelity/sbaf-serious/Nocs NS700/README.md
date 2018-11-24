# Nocs NS700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -2.0; 23 -2.5; 25 -2.9; 28 -3.4; 31 -3.8; 34 -4.2; 37 -4.4; 41 -4.6; 45 -4.8; 49 -4.8; 54 -5.0; 60 -5.1; 66 -5.2; 72 -5.4; 79 -5.4; 87 -5.5; 96 -5.0; 106 -4.2; 116 -3.4; 128 -4.3; 141 -4.4; 155 -3.9; 170 -2.5; 187 -1.9; 206 -0.7; 227 0.5; 249 1.5; 274 1.9; 302 1.2; 332 -1.1; 365 -2.1; 402 -1.8; 442 -1.6; 486 -1.6; 535 -1.3; 588 -0.9; 647 -0.8; 712 -0.6; 783 -0.3; 861 -0.2; 947 -0.0; 1042 0.4; 1146 0.9; 1261 1.4; 1387 1.2; 1526 0.5; 1678 1.1; 1846 1.5; 2031 1.7; 2234 1.4; 2457 1.2; 2703 0.3; 2973 -0.8; 3270 -1.3; 3597 -1.1; 3957 0.9; 4353 2.8; 4788 1.6; 5267 0.6; 5793 2.5; 6373 2.6; 7010 0.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.69 | -4.4 dB |
| Peaking | 102 Hz  | 1.16 | -3.3 dB |
| Peaking | 466 Hz  | 2.87 | -1.7 dB |
| Peaking | 1768 Hz | 1.51 | 1.5 dB  |
| Peaking | 6062 Hz | 4.71 | 3.1 dB  |
| Peaking | 153 Hz  | 4.64 | -1.8 dB |
| Peaking | 274 Hz  | 2.63 | 3.3 dB  |
| Peaking | 352 Hz  | 4.19 | -2.3 dB |
| Peaking | 3340 Hz | 4.35 | -2.0 dB |
| Peaking | 4378 Hz | 7.32 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS700/Nocs%20NS700.png)