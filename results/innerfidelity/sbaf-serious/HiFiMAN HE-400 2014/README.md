# HiFiMAN HE-400 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 0.0; 23 3.1; 25 3.0; 28 2.9; 31 2.8; 34 2.7; 37 2.7; 41 2.6; 45 2.6; 49 2.5; 54 2.4; 60 2.2; 66 1.9; 72 1.3; 79 0.8; 87 0.4; 96 0.0; 106 -0.3; 116 -0.4; 128 -0.8; 141 -0.9; 155 -1.0; 170 -1.1; 187 -1.3; 206 -1.6; 227 -1.7; 249 -2.0; 274 -2.1; 302 -2.2; 332 -2.0; 365 -1.6; 402 -1.4; 442 -1.8; 486 -2.4; 535 -2.4; 588 -1.9; 647 -1.3; 712 -1.6; 783 -1.5; 861 -1.1; 947 -0.4; 1042 0.1; 1146 0.5; 1261 1.3; 1387 1.5; 1526 1.7; 1678 1.9; 1846 1.4; 2031 0.5; 2234 0.2; 2457 -0.1; 2703 -1.0; 2973 -1.0; 3270 -0.1; 3597 -0.3; 3957 0.8; 4353 -2.2; 4788 -1.7; 5267 -0.1; 5793 1.1; 6373 -2.6; 7010 -3.5; 7711 -4.0; 8482 -5.5; 9330 -3.8; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.4; 20000 -4.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-400 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-400 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.8  | 3.1 dB  |
| Peaking | 54 Hz    | 1.78 | 1.7 dB  |
| Peaking | 245 Hz   | 0.9  | -2.0 dB |
| Peaking | 539 Hz   | 2.38 | -1.9 dB |
| Peaking | 8191 Hz  | 2.9  | -5.6 dB |
| Peaking | 802 Hz   | 4.39 | -1.2 dB |
| Peaking | 1556 Hz  | 1.88 | 2.1 dB  |
| Peaking | 2784 Hz  | 3.77 | -1.3 dB |
| Peaking | 10527 Hz | 6.35 | 1.5 dB  |
| Peaking | 19844 Hz | 3.43 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-400%202014/HiFiMAN%20HE-400%202014.png)