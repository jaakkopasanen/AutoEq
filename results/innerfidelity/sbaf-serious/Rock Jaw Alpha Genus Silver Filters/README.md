# Rock Jaw Alpha Genus Silver Filters
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 21 -11.6; 23 -11.8; 25 -11.8; 28 -11.9; 31 -11.9; 34 -11.8; 37 -11.8; 41 -11.7; 45 -11.6; 49 -11.5; 54 -11.4; 60 -11.3; 66 -11.2; 72 -11.1; 79 -11.0; 87 -10.9; 96 -10.8; 106 -10.5; 116 -10.1; 128 -9.9; 141 -9.6; 155 -9.2; 170 -8.7; 187 -8.3; 206 -7.7; 227 -7.1; 249 -6.5; 274 -5.9; 302 -5.2; 332 -4.6; 365 -3.9; 402 -3.3; 442 -2.5; 486 -2.1; 535 -1.4; 588 -0.6; 647 -0.2; 712 0.1; 783 0.5; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.8; 1526 -2.7; 1678 -3.9; 1846 -4.7; 2031 -5.3; 2234 -5.8; 2457 -5.9; 2703 -5.6; 2973 -3.6; 3270 -1.2; 3597 -0.5; 3957 -1.5; 4353 -5.6; 4788 -9.8; 5267 -8.6; 5793 -3.7; 6373 0.9; 7010 2.2; 7711 0.3; 8482 0.0; 9330 -0.6; 10263 -3.2; 11289 -2.4; 12418 -1.0; 13660 -1.3; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Jaw Alpha Genus Silver Filters GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Jaw Alpha Genus Silver Filters ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.1  | -11.8 dB |
| Peaking | 704 Hz   | 0.85 | 2.7 dB   |
| Peaking | 2180 Hz  | 1.69 | -6.3 dB  |
| Peaking | 4954 Hz  | 5.59 | -11.0 dB |
| Peaking | 21998 Hz | 1.27 | -1.9 dB  |
| Peaking | 2982 Hz  | 2.99 | -2.1 dB  |
| Peaking | 3411 Hz  | 4.3  | 3.5 dB   |
| Peaking | 5700 Hz  | 3.48 | -2.8 dB  |
| Peaking | 6640 Hz  | 3.61 | 4.6 dB   |
| Peaking | 10679 Hz | 3.82 | -3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Rock%20Jaw%20Alpha%20Genus%20Silver%20Filters/Rock%20Jaw%20Alpha%20Genus%20Silver%20Filters.png)