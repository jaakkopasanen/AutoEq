# FLC Technologies FLC8 G G Bk De
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.2; 23 -0.4; 25 -0.5; 28 -0.6; 31 -0.6; 34 -0.6; 37 -0.6; 41 -0.6; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.6; 66 -0.6; 72 -0.7; 79 -0.8; 87 -0.9; 96 -1.1; 106 -1.1; 116 -1.0; 128 -1.1; 141 -1.1; 155 -1.1; 170 -1.0; 187 -0.9; 206 -0.8; 227 -0.6; 249 -0.5; 274 -0.3; 302 -0.1; 332 0.1; 365 0.3; 402 0.5; 442 0.8; 486 0.8; 535 1.0; 588 1.4; 647 1.4; 712 1.3; 783 1.4; 861 1.2; 947 0.5; 1042 -0.4; 1146 -1.0; 1261 -1.2; 1387 -1.2; 1526 -0.6; 1678 0.2; 1846 1.4; 2031 2.1; 2234 2.3; 2457 2.6; 2703 2.2; 2973 4.6; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 4.3; 7010 -0.5; 7711 -2.6; 8482 -2.4; 9330 -2.1; 10263 -2.2; 11289 -0.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 G G Bk De GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 G G Bk De ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 707 Hz  | 1.7  | 1.7 dB  |
| Peaking | 1299 Hz | 2.22 | -2.4 dB |
| Peaking | 4031 Hz | 1.01 | 6.7 dB  |
| Peaking | 6003 Hz | 3.05 | 5.9 dB  |
| Peaking | 7608 Hz | 1.49 | -6.0 dB |
| Peaking | 40 Hz   | 0.46 | -0.5 dB |
| Peaking | 137 Hz  | 1.03 | -1.0 dB |
| Peaking | 2024 Hz | 5.4  | 0.6 dB  |
| Peaking | 2812 Hz | 5.59 | -2.1 dB |
| Peaking | 3075 Hz | 7.73 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20G%20G%20Bk%20De/FLC%20Technologies%20FLC8%20G%20G%20Bk%20De.png)