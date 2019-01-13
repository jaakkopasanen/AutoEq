# Stax SR-404 S 2742
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.7; 37 5.6; 41 5.5; 45 5.4; 49 5.4; 54 5.3; 60 5.0; 66 4.6; 72 4.3; 79 4.0; 87 3.8; 96 3.4; 106 3.0; 116 2.8; 128 2.6; 141 2.4; 155 2.3; 170 2.3; 187 2.1; 206 2.1; 227 2.1; 249 2.0; 274 2.0; 302 2.0; 332 2.0; 365 2.1; 402 2.1; 442 2.2; 486 1.9; 535 1.7; 588 2.0; 647 1.7; 712 1.5; 783 1.5; 861 1.0; 947 0.5; 1042 -0.1; 1146 -0.5; 1261 -1.6; 1387 -2.5; 1526 -3.1; 1678 -3.9; 1846 -2.5; 2031 0.4; 2234 2.8; 2457 4.3; 2703 2.9; 2973 0.9; 3270 1.1; 3597 1.7; 3957 3.1; 4353 3.1; 4788 2.2; 5267 2.2; 5793 0.5; 6373 0.4; 7010 2.4; 7711 0.3; 8482 -2.1; 9330 -4.2; 10263 -1.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.8; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-404 S 2742 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 S 2742 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.27 | 6.0 dB   |
| Peaking | 524 Hz  | 0.54 | 2.1 dB   |
| Peaking | 1753 Hz | 1    | -20.7 dB |
| Peaking | 2017 Hz | 0.77 | 18.0 dB  |
| Peaking | 9208 Hz | 5.5  | -5.4 dB  |
| Peaking | 2121 Hz | 3.97 | -0.9 dB  |
| Peaking | 2442 Hz | 4.16 | 2.7 dB   |
| Peaking | 3049 Hz | 3.41 | -2.7 dB  |
| Peaking | 4200 Hz | 5.16 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-404%20S%202742/Stax%20SR-404%20S%202742.png)