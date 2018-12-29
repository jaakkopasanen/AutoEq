# Beyerdynamic DT 231
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 5.6; 141 5.1; 155 4.7; 170 4.6; 187 5.1; 206 5.0; 227 4.6; 249 4.2; 274 3.9; 302 3.7; 332 3.4; 365 3.1; 402 2.8; 442 2.8; 486 2.4; 535 2.1; 588 1.9; 647 1.5; 712 1.2; 783 0.4; 861 -0.1; 947 -0.3; 1042 -0.1; 1146 0.5; 1261 1.0; 1387 0.8; 1526 -1.4; 1678 -4.6; 1846 -4.8; 2031 -1.0; 2234 1.8; 2457 4.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 3.6; 4788 -4.0; 5267 -1.8; 5793 2.7; 6373 3.2; 7010 0.4; 7711 -3.3; 8482 -3.7; 9330 -0.1; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -6.3; 15026 -7.8; 16529 -4.4; 18182 -2.1; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 231 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 231 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.18 | 5.6 dB  |
| Peaking | 149 Hz   | 0.37 | 4.4 dB  |
| Peaking | 1785 Hz  | 4.41 | -7.5 dB |
| Peaking | 3018 Hz  | 1.78 | 7.3 dB  |
| Peaking | 15015 Hz | 2.19 | -8.4 dB |
| Peaking | 4179 Hz  | 5.39 | 5.9 dB  |
| Peaking | 4854 Hz  | 4.27 | -8.5 dB |
| Peaking | 6103 Hz  | 3.58 | 4.8 dB  |
| Peaking | 8015 Hz  | 4.99 | -5.1 dB |
| Peaking | 11663 Hz | 3.58 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20231/Beyerdynamic%20DT%20231.png)