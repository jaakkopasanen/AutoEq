# Beyerdynamic DT 880 250 Ohm balanced
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 5.2; 49 4.8; 54 4.2; 60 3.7; 66 3.7; 72 3.7; 79 2.5; 87 1.3; 96 0.5; 106 -0.1; 116 -0.7; 128 -1.4; 141 -2.0; 155 -2.5; 170 -2.8; 187 -3.2; 206 -3.5; 227 -3.5; 249 -3.5; 274 -3.7; 302 -3.5; 332 -3.2; 365 -2.9; 402 -2.6; 442 -2.3; 486 -1.3; 535 -1.5; 588 -1.3; 647 -0.8; 712 -0.7; 783 -0.5; 861 -0.4; 947 -0.1; 1042 0.2; 1146 0.8; 1261 1.3; 1387 1.1; 1526 0.5; 1678 0.0; 1846 -0.4; 2031 -0.3; 2234 -0.1; 2457 0.3; 2703 -0.2; 2973 -0.9; 3270 -1.1; 3597 -0.6; 3957 0.2; 4353 1.0; 4788 0.5; 5267 -1.2; 5793 -3.6; 6373 -4.1; 7010 -2.7; 7711 -3.3; 8482 -5.0; 9330 -4.4; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 250 Ohm balanced GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 250 Ohm balanced ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.35 | 6.5 dB  |
| Peaking | 209 Hz  | 0.56 | -4.9 dB |
| Peaking | 2600 Hz | 0.1  | 0.5 dB  |
| Peaking | 6182 Hz | 4.13 | -4.4 dB |
| Peaking | 8668 Hz | 3.8  | -5.7 dB |
| Peaking | 1293 Hz | 3.63 | 1.4 dB  |
| Peaking | 1861 Hz | 3.58 | -0.8 dB |
| Peaking | 3268 Hz | 3.55 | -1.6 dB |
| Peaking | 4546 Hz | 3.17 | 1.4 dB  |
| Peaking | 5549 Hz | 7.54 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20880%20250%20Ohm%20balanced/Beyerdynamic%20DT%20880%20250%20Ohm%20balanced.png)