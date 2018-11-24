# Stax SR-404 Ltd SSL-0670

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.4; 28 5.2; 31 5.1; 34 5.0; 37 5.0; 41 5.0; 45 5.0; 49 5.0; 54 5.0; 60 4.9; 66 4.5; 72 4.0; 79 3.8; 87 3.6; 96 3.3; 106 2.9; 116 2.7; 128 2.4; 141 2.3; 155 2.1; 170 2.1; 187 1.9; 206 1.8; 227 1.8; 249 1.8; 274 1.8; 302 1.9; 332 2.0; 365 1.9; 402 1.9; 442 2.0; 486 1.8; 535 1.6; 588 1.7; 647 1.6; 712 1.2; 783 1.3; 861 0.7; 947 0.4; 1042 -0.1; 1146 -0.6; 1261 -1.4; 1387 -2.4; 1526 -3.1; 1678 -3.5; 1846 -2.2; 2031 0.3; 2234 1.9; 2457 2.0; 2703 1.1; 2973 0.9; 3270 1.1; 3597 1.0; 3957 3.1; 4353 2.5; 4788 1.9; 5267 2.9; 5793 0.7; 6373 2.4; 7010 2.5; 7711 0.3; 8482 -1.4; 9330 -3.7; 10263 -2.1; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.1; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-404 Ltd SSL-0670 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 Ltd SSL-0670 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 12 Hz    |  0.48 | 3.5 dB  |
| Peaking | 48 Hz    |  0.4  | 4.0 dB  |
| Peaking | 1514 Hz  |  1.53 | -6.2 dB |
| Peaking | 1926 Hz  |  0.2  | 3.0 dB  |
| Peaking | 9399 Hz  |  3.84 | -5.4 dB |
| Peaking | 2309 Hz  |  3.79 | 3.0 dB  |
| Peaking | 2808 Hz  |  1.15 | -1.7 dB |
| Peaking | 4116 Hz  |  7.9  | 2.2 dB  |
| Peaking | 6746 Hz  | 12.41 | 3.0 dB  |
| Peaking | 19513 Hz |  1.9  | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-404%20Ltd%20SSL-0670/Stax%20SR-404%20Ltd%20SSL-0670.png)