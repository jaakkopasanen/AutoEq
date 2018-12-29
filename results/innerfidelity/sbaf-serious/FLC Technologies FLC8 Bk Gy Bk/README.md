# FLC Technologies FLC8 Bk Gy Bk
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.0; 23 -2.2; 25 -2.3; 28 -2.5; 31 -2.6; 34 -2.6; 37 -2.6; 41 -2.6; 45 -2.6; 49 -2.7; 54 -2.7; 60 -2.7; 66 -2.8; 72 -2.8; 79 -2.9; 87 -3.1; 96 -3.1; 106 -3.1; 116 -3.0; 128 -2.9; 141 -2.9; 155 -2.8; 170 -2.6; 187 -2.4; 206 -2.3; 227 -2.0; 249 -1.8; 274 -1.5; 302 -1.2; 332 -0.9; 365 -0.7; 402 -0.4; 442 -0.0; 486 0.1; 535 0.3; 588 0.8; 647 0.9; 712 0.8; 783 1.2; 861 1.0; 947 0.4; 1042 -0.2; 1146 -0.5; 1261 -0.6; 1387 -0.6; 1526 -0.2; 1678 0.5; 1846 1.6; 2031 2.3; 2234 2.5; 2457 2.9; 2703 2.7; 2973 4.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.9; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.8; 7010 0.2; 7711 -3.5; 8482 -5.2; 9330 -5.4; 10263 -3.8; 11289 -0.4; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 Bk Gy Bk GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 Bk Gy Bk ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.63 | -1.9 dB  |
| Peaking | 120 Hz  | 0.49 | -2.8 dB  |
| Peaking | 625 Hz  | 2.53 | 1.2 dB   |
| Peaking | 5249 Hz | 0.78 | 8.5 dB   |
| Peaking | 8563 Hz | 1.86 | -10.6 dB |
| Peaking | 827 Hz  | 6.24 | 1.0 dB   |
| Peaking | 1322 Hz | 2.6  | -1.7 dB  |
| Peaking | 3249 Hz | 5.48 | 2.0 dB   |
| Peaking | 5723 Hz | 1.75 | -1.5 dB  |
| Peaking | 6154 Hz | 5.63 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20Bk%20Gy%20Bk/FLC%20Technologies%20FLC8%20Bk%20Gy%20Bk.png)