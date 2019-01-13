# Audeo PFE 121 Gray Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.4; 25 5.1; 28 4.7; 31 4.4; 34 4.1; 37 3.8; 41 3.5; 45 3.2; 49 2.9; 54 2.6; 60 2.2; 66 1.8; 72 1.5; 79 0.9; 87 0.5; 96 0.1; 106 -0.2; 116 -0.4; 128 -0.7; 141 -1.1; 155 -1.1; 170 -1.3; 187 -1.3; 206 -1.4; 227 -1.2; 249 -1.2; 274 -1.1; 302 -0.9; 332 -0.7; 365 -0.5; 402 -0.3; 442 0.2; 486 0.3; 535 0.5; 588 1.0; 647 1.2; 712 1.1; 783 1.2; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.0; 1526 -2.8; 1678 -3.2; 1846 -3.2; 2031 -3.0; 2234 -2.7; 2457 -1.6; 2703 -0.8; 2973 1.3; 3270 3.4; 3597 4.3; 3957 3.6; 4353 1.2; 4788 0.7; 5267 2.3; 5793 3.7; 6373 4.7; 7010 2.5; 7711 0.3; 8482 -0.6; 9330 -3.1; 10263 -2.8; 11289 -0.1; 12418 0.0; 13660 -0.8; 15026 -4.8; 16529 -0.9; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeo PFE 121 Gray Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Gray Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.87 | 5.5 dB  |
| Peaking | 1889 Hz  | 1.88 | -3.6 dB |
| Peaking | 3566 Hz  | 3.1  | 5.8 dB  |
| Peaking | 6297 Hz  | 2.95 | 6.7 dB  |
| Peaking | 9408 Hz  | 0.39 | -2.3 dB |
| Peaking | 201 Hz   | 1.08 | -1.6 dB |
| Peaking | 695 Hz   | 2.05 | 1.7 dB  |
| Peaking | 9704 Hz  | 4.66 | -3.3 dB |
| Peaking | 14271 Hz | 1.05 | 4.6 dB  |
| Peaking | 15002 Hz | 3.02 | -8.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Gray%20Filter/Audeo%20PFE%20121%20Gray%20Filter.png)