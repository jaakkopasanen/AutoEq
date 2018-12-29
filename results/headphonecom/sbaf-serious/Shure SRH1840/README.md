# Shure SRH1840
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.6; 54 5.3; 60 4.9; 66 4.5; 72 4.3; 79 4.5; 87 3.9; 96 3.0; 106 2.4; 116 1.9; 128 1.4; 141 1.0; 155 0.6; 170 0.4; 187 0.1; 206 -0.1; 227 -0.1; 249 -0.2; 274 -0.3; 302 -0.2; 332 -0.2; 365 0.0; 402 -0.1; 442 0.1; 486 0.3; 535 0.5; 588 0.7; 647 0.7; 712 0.9; 783 1.4; 861 0.5; 947 0.2; 1042 -0.0; 1146 -0.1; 1261 -0.5; 1387 -1.2; 1526 -2.1; 1678 -2.7; 1846 -4.0; 2031 -4.7; 2234 -5.1; 2457 -4.9; 2703 -4.8; 2973 -4.7; 3270 -4.4; 3597 -3.8; 3957 -3.3; 4353 -2.4; 4788 -1.1; 5267 0.9; 5793 0.3; 6373 -1.3; 7010 0.5; 7711 -0.2; 8482 -3.5; 9330 -4.1; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1840 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.5  | 6.5 dB  |
| Peaking | 1100 Hz | 0.79 | 5.0 dB  |
| Peaking | 2592 Hz | 0.39 | -8.6 dB |
| Peaking | 5776 Hz | 0.7  | 5.3 dB  |
| Peaking | 8911 Hz | 5.45 | -5.7 dB |
| Peaking | 82 Hz   | 3.89 | 1.3 dB  |
| Peaking | 211 Hz  | 0.95 | -0.8 dB |
| Peaking | 629 Hz  | 1.91 | 0.7 dB  |
| Peaking | 5379 Hz | 7.22 | 1.9 dB  |
| Peaking | 6247 Hz | 9.81 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)