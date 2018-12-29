# Beyerdynamic T90 250 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 0.0; 23 0.8; 25 0.6; 28 0.4; 31 0.2; 34 -0.0; 37 -0.2; 41 -0.2; 45 -0.2; 49 -0.2; 54 -0.1; 60 0.7; 66 -0.7; 72 -1.7; 79 -2.3; 87 -2.6; 96 -3.0; 106 -3.3; 116 -3.7; 128 -4.1; 141 -4.5; 155 -4.7; 170 -4.6; 187 -4.9; 206 -4.9; 227 -4.9; 249 -4.8; 274 -4.7; 302 -4.4; 332 -4.1; 365 -3.7; 402 -3.2; 442 -3.0; 486 -2.5; 535 -1.9; 588 -1.1; 647 -0.9; 712 -0.1; 783 0.2; 861 0.6; 947 0.3; 1042 0.1; 1146 -0.2; 1261 -0.5; 1387 -1.5; 1526 -2.2; 1678 -2.7; 1846 -3.5; 2031 -3.7; 2234 -3.3; 2457 -3.4; 2703 -3.9; 2973 -4.7; 3270 -5.1; 3597 -4.5; 3957 -4.4; 4353 -4.1; 4788 3.2; 5267 1.6; 5793 -1.1; 6373 -8.1; 7010 -8.7; 7711 -10.2; 8482 -11.4; 9330 -11.2; 10263 -9.2; 11289 -8.2; 12418 -7.9; 13660 -5.0; 15026 -2.9; 16529 -6.7; 18182 -9.4; 20000 -0.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T90 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T90 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 201 Hz   | 0.65 | -5.3 dB  |
| Peaking | 1979 Hz  | 2.64 | -3.2 dB  |
| Peaking | 3187 Hz  | 3.44 | -4.3 dB  |
| Peaking | 9061 Hz  | 1.45 | -11.9 dB |
| Peaking | 17978 Hz | 1.71 | -9.2 dB  |
| Peaking | 872 Hz   | 1.77 | 2.0 dB   |
| Peaking | 2374 Hz  | 0.14 | -0.7 dB  |
| Peaking | 4252 Hz  | 4.14 | -7.6 dB  |
| Peaking | 4943 Hz  | 2.6  | 10.3 dB  |
| Peaking | 6630 Hz  | 5.48 | -5.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T90%20250%20Ohm/Beyerdynamic%20T90%20250%20Ohm.png)