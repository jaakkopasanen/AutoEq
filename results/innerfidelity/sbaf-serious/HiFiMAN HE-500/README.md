# HiFiMAN HE-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 0.0; 23 3.3; 25 2.9; 28 2.6; 31 2.4; 34 2.4; 37 2.4; 41 2.3; 45 2.3; 49 2.3; 54 2.2; 60 2.0; 66 1.8; 72 1.6; 79 1.4; 87 1.1; 96 0.9; 106 0.7; 116 0.7; 128 0.3; 141 0.1; 155 -0.1; 170 -0.0; 187 -0.0; 206 -0.2; 227 -0.2; 249 -0.2; 274 -0.4; 302 -0.4; 332 -0.2; 365 -0.4; 402 -0.7; 442 -0.3; 486 -0.4; 535 -0.2; 588 -0.1; 647 -0.0; 712 -0.0; 783 0.9; 861 0.2; 947 -0.1; 1042 -0.2; 1146 0.2; 1261 0.2; 1387 1.1; 1526 1.1; 1678 1.7; 1846 2.8; 2031 2.2; 2234 2.1; 2457 2.6; 2703 2.2; 2973 2.2; 3270 1.4; 3597 1.2; 3957 1.3; 4353 -0.5; 4788 0.5; 5267 2.7; 5793 2.6; 6373 0.8; 7010 1.1; 7711 -0.1; 8482 -4.0; 9330 -5.5; 10263 -0.7; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.3; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 16 Hz   |  0.79 | 3.8 dB  |
| Peaking | 57 Hz   |  1.27 | 1.7 dB  |
| Peaking | 2288 Hz |  1.4  | 2.7 dB  |
| Peaking | 5593 Hz |  5.66 | 3.2 dB  |
| Peaking | 9071 Hz |  5.86 | -6.6 dB |
| Peaking | 24 Hz   |  0.65 | 0.4 dB  |
| Peaking | 327 Hz  |  3.69 | 0.9 dB  |
| Peaking | 339 Hz  |  1.56 | -1.2 dB |
| Peaking | 4459 Hz | 11.49 | -1.6 dB |
| Peaking | 7201 Hz |  9.2  | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-500/HiFiMAN%20HE-500.png)