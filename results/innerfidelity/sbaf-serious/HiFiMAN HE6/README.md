# HiFiMAN HE6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 0.0; 23 3.8; 25 3.5; 28 3.3; 31 3.1; 34 3.0; 37 3.0; 41 3.0; 45 2.9; 49 2.8; 54 2.8; 60 2.8; 66 2.7; 72 2.3; 79 2.0; 87 1.8; 96 1.4; 106 1.2; 116 1.1; 128 0.9; 141 0.7; 155 0.6; 170 0.6; 187 0.6; 206 0.6; 227 0.7; 249 0.6; 274 0.6; 302 0.5; 332 0.3; 365 0.2; 402 0.2; 442 0.4; 486 0.2; 535 0.2; 588 0.5; 647 0.4; 712 0.1; 783 0.3; 861 -0.0; 947 -0.3; 1042 0.1; 1146 1.0; 1261 0.7; 1387 1.0; 1526 1.7; 1678 2.2; 1846 3.2; 2031 2.9; 2234 2.3; 2457 2.8; 2703 2.1; 2973 1.1; 3270 -0.0; 3597 0.1; 3957 -1.5; 4353 -1.3; 4788 0.1; 5267 -2.1; 5793 -5.7; 6373 -4.8; 7010 -3.8; 7711 -3.3; 8482 -6.1; 9330 -7.0; 10263 -2.2; 11289 0.0; 12418 -0.0; 13660 -2.1; 15026 -2.5; 16529 -0.6; 18182 -0.4; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 1.06 | 3.6 dB  |
| Peaking | 51 Hz    | 0.6  | 2.5 dB  |
| Peaking | 2048 Hz  | 1.69 | 3.2 dB  |
| Peaking | 6067 Hz  | 3.26 | -5.4 dB |
| Peaking | 8998 Hz  | 4.15 | -7.4 dB |
| Peaking | 2610 Hz  | 7.24 | 0.8 dB  |
| Peaking | 4164 Hz  | 4.43 | -1.3 dB |
| Peaking | 4912 Hz  | 9.53 | 2.6 dB  |
| Peaking | 11265 Hz | 3.97 | 2.4 dB  |
| Peaking | 18701 Hz | 0.33 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE6/HiFiMAN%20HE6.png)