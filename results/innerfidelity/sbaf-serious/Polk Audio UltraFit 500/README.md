# Polk Audio UltraFit 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.9; 66 5.0; 72 4.2; 79 3.3; 87 2.5; 96 1.5; 106 1.0; 116 0.5; 128 -0.5; 141 -0.9; 155 -1.5; 170 -2.0; 187 -2.6; 206 -3.1; 227 -3.5; 249 -3.8; 274 -4.1; 302 -4.3; 332 -4.6; 365 -4.8; 402 -5.5; 442 -4.8; 486 -4.8; 535 -5.0; 588 -4.5; 647 -4.0; 712 -3.6; 783 -2.5; 861 -1.6; 947 -0.6; 1042 0.5; 1146 1.6; 1261 2.8; 1387 3.7; 1526 4.6; 1678 5.8; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFit 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.44 | 6.9 dB  |
| Peaking | 469 Hz  | 0.33 | -6.3 dB |
| Peaking | 1764 Hz | 0.77 | 8.1 dB  |
| Peaking | 3944 Hz | 1.56 | 3.9 dB  |
| Peaking | 5815 Hz | 3.54 | 4.1 dB  |
| Peaking | 55 Hz   | 1.06 | -1.1 dB |
| Peaking | 60 Hz   | 2.52 | 1.9 dB  |
| Peaking | 6566 Hz | 7.91 | 2.0 dB  |
| Peaking | 7993 Hz | 2.27 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%20500/Polk%20Audio%20UltraFit%20500.png)