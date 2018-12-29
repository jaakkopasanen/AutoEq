# Koss Porta Pro sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.0; 34 4.1; 37 3.2; 41 2.2; 45 1.3; 49 0.4; 54 -0.6; 60 -1.7; 66 -2.6; 72 -3.5; 79 -4.3; 87 -4.9; 96 -5.5; 106 -5.9; 116 -5.9; 128 -6.0; 141 -5.9; 155 -5.9; 170 -5.7; 187 -5.2; 206 -4.7; 227 -4.3; 249 -3.9; 274 -3.5; 302 -3.1; 332 -2.7; 365 -2.1; 402 -1.4; 442 -1.1; 486 -1.0; 535 -0.6; 588 -0.3; 647 -0.0; 712 0.0; 783 0.2; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.7; 1387 -1.4; 1526 -2.4; 1678 -3.2; 1846 -4.0; 2031 -4.7; 2234 -4.7; 2457 -3.4; 2703 -1.3; 2973 1.0; 3270 2.6; 3597 3.3; 3957 1.6; 4353 -0.2; 4788 -2.2; 5267 -0.4; 5793 2.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -3.0; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.81 | 7.0 dB  |
| Peaking | 122 Hz  | 0.59 | -6.8 dB |
| Peaking | 2113 Hz | 2.2  | -5.6 dB |
| Peaking | 3243 Hz | 2.93 | 2.3 dB  |
| Peaking | 3529 Hz | 4.02 | 2.2 dB  |
| Peaking | 820 Hz  | 1.41 | 0.9 dB  |
| Peaking | 1578 Hz | 5.16 | -0.9 dB |
| Peaking | 4851 Hz | 5.51 | -3.1 dB |
| Peaking | 6322 Hz | 5.1  | 6.2 dB  |
| Peaking | 9236 Hz | 7.89 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro%20sample%202/Koss%20Porta%20Pro%20sample%202.png)