# Denon AH-C710
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.4dB
GraphicEQ: 21 -12.1; 23 -12.0; 25 -11.9; 28 -11.9; 31 -11.9; 34 -11.8; 37 -11.8; 41 -11.7; 45 -11.6; 49 -11.6; 54 -11.6; 60 -11.5; 66 -11.5; 72 -11.4; 79 -11.4; 87 -11.2; 96 -11.1; 106 -10.8; 116 -10.6; 128 -10.3; 141 -10.0; 155 -9.6; 170 -9.2; 187 -8.7; 206 -8.2; 227 -7.5; 249 -6.9; 274 -6.3; 302 -5.5; 332 -4.8; 365 -4.3; 402 -3.6; 442 -3.0; 486 -2.3; 535 -1.7; 588 -1.1; 647 -0.5; 712 -0.1; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.7; 1387 -1.4; 1526 -2.2; 1678 -2.7; 1846 -3.0; 2031 -3.7; 2234 -4.3; 2457 -5.2; 2703 -6.1; 2973 -5.5; 3270 -3.0; 3597 -0.5; 3957 -0.7; 4353 -2.7; 4788 -4.4; 5267 -6.2; 5793 -10.3; 6373 -7.7; 7010 -3.3; 7711 -1.2; 8482 -1.3; 9330 -3.8; 10263 -4.1; 11289 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C710 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-4**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C710 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.2  | -11.8 dB |
| Peaking | 172 Hz  | 0.68 | -4.3 dB  |
| Peaking | 2540 Hz | 2.08 | -5.8 dB  |
| Peaking | 5897 Hz | 4    | -10.7 dB |
| Peaking | 9736 Hz | 6.25 | -4.7 dB  |
| Peaking | 388 Hz  | 1.57 | -0.8 dB  |
| Peaking | 804 Hz  | 1.19 | 1.5 dB   |
| Peaking | 1629 Hz | 3.14 | -1.5 dB  |
| Peaking | 3781 Hz | 7.12 | 2.3 dB   |
| Peaking | 4745 Hz | 6.49 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C710/Denon%20AH-C710.png)