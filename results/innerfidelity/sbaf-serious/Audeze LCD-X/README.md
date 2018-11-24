# Audeze LCD-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.0; 25 3.9; 28 3.6; 31 3.0; 34 2.3; 37 1.6; 41 1.2; 45 1.1; 49 1.0; 54 0.9; 60 0.8; 66 0.8; 72 0.6; 79 0.4; 87 0.1; 96 -0.2; 106 -0.4; 116 -0.6; 128 -0.9; 141 -1.2; 155 -1.3; 170 -1.5; 187 -1.7; 206 -1.8; 227 -1.7; 249 -1.8; 274 -1.7; 302 -1.6; 332 -1.4; 365 -1.1; 402 -1.0; 442 -0.7; 486 -1.2; 535 -1.1; 588 -0.6; 647 -0.7; 712 -0.7; 783 -0.4; 861 -0.2; 947 0.0; 1042 0.1; 1146 0.2; 1261 0.0; 1387 -0.6; 1526 -0.7; 1678 -0.8; 1846 -0.8; 2031 -0.9; 2234 -0.6; 2457 0.7; 2703 2.4; 2973 4.2; 3270 5.3; 3597 5.3; 3957 3.5; 4353 3.2; 4788 2.6; 5267 5.7; 5793 5.7; 6373 3.5; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.1; 16529 -1.6; 18182 -3.3; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.52 | 4.7 dB  |
| Peaking | 240 Hz   | 0.58 | -1.8 dB |
| Peaking | 3381 Hz  | 3.36 | 5.7 dB  |
| Peaking | 5639 Hz  | 3.34 | 5.9 dB  |
| Peaking | 19625 Hz | 1.25 | -4.8 dB |
| Peaking | 1085 Hz  | 3.61 | 0.7 dB  |
| Peaking | 2054 Hz  | 1.68 | -1.6 dB |
| Peaking | 2778 Hz  | 4.39 | 1.6 dB  |
| Peaking | 8221 Hz  | 6.37 | -0.6 dB |
| Peaking | 14454 Hz | 3.69 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)