# 1MORE Multi Unit Earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.6; 23 -1.1; 25 -1.5; 28 -2.0; 31 -2.5; 34 -2.8; 37 -3.1; 41 -3.4; 45 -3.7; 49 -4.0; 54 -4.3; 60 -4.6; 66 -4.9; 72 -5.2; 79 -5.4; 87 -5.7; 96 -5.9; 106 -6.0; 116 -6.0; 128 -6.1; 141 -6.0; 155 -5.9; 170 -5.7; 187 -5.4; 206 -5.2; 227 -4.7; 249 -4.3; 274 -3.9; 302 -3.4; 332 -2.9; 365 -2.3; 402 -1.8; 442 -1.2; 486 -0.9; 535 -0.4; 588 0.3; 647 0.6; 712 0.7; 783 0.9; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.3; 1387 -2.4; 1526 -3.6; 1678 -4.7; 1846 -5.5; 2031 -5.9; 2234 -5.7; 2457 -3.7; 2703 -1.3; 2973 1.2; 3270 2.3; 3597 1.4; 3957 -1.6; 4353 -1.9; 4788 3.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -3.7; 11289 -2.5; 12418 -0.1; 13660 -0.1; 15026 -1.8; 16529 -3.7; 18182 -4.0; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Multi Unit Earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Multi Unit Earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 83 Hz    | 0.54 | -5.1 dB |
| Peaking | 195 Hz   | 1.07 | -3.1 dB |
| Peaking | 1959 Hz  | 2.5  | -6.7 dB |
| Peaking | 5819 Hz  | 2.76 | 7.7 dB  |
| Peaking | 19212 Hz | 0.25 | -3.0 dB |
| Peaking | 749 Hz   | 2.61 | 1.7 dB  |
| Peaking | 3274 Hz  | 5.24 | 3.3 dB  |
| Peaking | 4166 Hz  | 9.13 | -4.5 dB |
| Peaking | 10471 Hz | 5.63 | -3.1 dB |
| Peaking | 13181 Hz | 3.38 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Multi%20Unit%20Earphones/1MORE%20Multi%20Unit%20Earphones.png)