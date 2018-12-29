# Shure SRH1540
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -3.7; 23 -4.4; 25 -4.9; 28 -5.6; 31 -6.1; 34 -6.5; 37 -6.8; 41 -7.2; 45 -7.5; 49 -7.6; 54 -7.7; 60 -7.8; 66 -7.7; 72 -7.4; 79 -6.9; 87 -6.4; 96 -6.0; 106 -5.9; 116 -5.9; 128 -5.7; 141 -5.2; 155 -4.1; 170 -3.0; 187 -3.7; 206 -3.5; 227 -3.9; 249 -4.1; 274 -4.1; 302 -4.4; 332 -4.5; 365 -4.2; 402 -3.6; 442 -3.0; 486 -2.5; 535 -2.1; 588 -1.6; 647 -0.9; 712 -0.4; 783 -0.0; 861 0.1; 947 0.2; 1042 -0.1; 1146 0.2; 1261 0.2; 1387 -0.5; 1526 -1.5; 1678 -2.5; 1846 -3.2; 2031 -3.2; 2234 -2.4; 2457 -1.8; 2703 -0.8; 2973 0.3; 3270 -0.1; 3597 0.3; 3957 -0.6; 4353 -1.0; 4788 -0.6; 5267 0.8; 5793 -1.6; 6373 -2.7; 7010 -0.9; 7711 -0.6; 8482 -2.4; 9330 -4.6; 10263 -2.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.7; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH1540 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1540 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.59 | -5.3 dB |
| Peaking | 89 Hz   | 0.58 | -3.9 dB |
| Peaking | 339 Hz  | 1.28 | -3.5 dB |
| Peaking | 9334 Hz | 4.03 | -4.8 dB |
| Peaking | 1686 Hz | 0.79 | 2.3 dB  |
| Peaking | 1908 Hz | 1.8  | -5.5 dB |
| Peaking | 6131 Hz | 8.46 | -1.1 dB |
| Peaking | 6219 Hz | 8.24 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH1540/Shure%20SRH1540.png)