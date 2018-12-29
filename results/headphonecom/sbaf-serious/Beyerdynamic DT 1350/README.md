# Beyerdynamic DT 1350
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.4; 23 -1.4; 25 -1.5; 28 -1.5; 31 -1.6; 34 -1.7; 37 -1.8; 41 -1.8; 45 -1.8; 49 -1.9; 54 -1.7; 60 -1.7; 66 -2.1; 72 -2.3; 79 -2.4; 87 -2.0; 96 -1.2; 106 -0.6; 116 -1.2; 128 -1.3; 141 -0.4; 155 -0.7; 170 -1.7; 187 -3.0; 206 -3.6; 227 -3.8; 249 -4.0; 274 -3.7; 302 -3.4; 332 -4.1; 365 -4.3; 402 -3.9; 442 -4.1; 486 -4.2; 535 -3.8; 588 -3.2; 647 -2.7; 712 -1.7; 783 -0.9; 861 -0.9; 947 -0.5; 1042 0.1; 1146 0.7; 1261 1.1; 1387 1.0; 1526 0.6; 1678 0.1; 1846 0.2; 2031 1.3; 2234 3.4; 2457 5.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.1; 4353 2.0; 4788 2.4; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.2; 8482 -7.1; 9330 -9.0; 10263 -1.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.66 | -2.0 dB  |
| Peaking | 361 Hz   | 0.78 | -4.5 dB  |
| Peaking | 2997 Hz  | 1.64 | 6.6 dB   |
| Peaking | 6063 Hz  | 2.76 | 6.2 dB   |
| Peaking | 8991 Hz  | 4.64 | -11.4 dB |
| Peaking | 149 Hz   | 4.11 | 1.5 dB   |
| Peaking | 200 Hz   | 3.77 | -1.4 dB  |
| Peaking | 1227 Hz  | 2.92 | 1.2 dB   |
| Peaking | 1814 Hz  | 5.46 | -1.7 dB  |
| Peaking | 10774 Hz | 9.25 | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%201350/Beyerdynamic%20DT%201350.png)