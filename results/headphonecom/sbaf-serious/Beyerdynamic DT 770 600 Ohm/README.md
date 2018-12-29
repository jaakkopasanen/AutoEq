# Beyerdynamic DT 770 600 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.4; 37 4.6; 41 3.5; 45 2.5; 49 1.6; 54 2.0; 60 2.2; 66 0.2; 72 -1.2; 79 0.1; 87 2.5; 96 0.5; 106 -1.2; 116 -2.2; 128 -3.1; 141 -3.6; 155 -3.7; 170 -3.4; 187 -4.2; 206 -4.0; 227 -3.9; 249 -3.6; 274 -3.4; 302 -3.1; 332 -2.8; 365 -2.5; 402 -2.2; 442 -2.0; 486 -1.6; 535 -1.2; 588 -1.0; 647 -0.8; 712 -0.1; 783 0.2; 861 -0.0; 947 -0.3; 1042 0.2; 1146 0.9; 1261 0.7; 1387 -0.1; 1526 -0.5; 1678 -0.9; 1846 -1.0; 2031 -0.7; 2234 -1.0; 2457 -2.1; 2703 -1.2; 2973 0.6; 3270 2.7; 3597 5.2; 3957 5.3; 4353 3.1; 4788 5.6; 5267 -3.9; 5793 -6.8; 6373 -6.3; 7010 -2.7; 7711 -4.9; 8482 -9.0; 9330 -8.2; 10263 -1.7; 11289 0.0; 12418 -2.1; 13660 -2.5; 15026 -0.4; 16529 -1.9; 18182 -6.1; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 770 600 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 770 600 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.64 | 6.3 dB   |
| Peaking | 203 Hz   | 0.76 | -4.4 dB  |
| Peaking | 4627 Hz  | 2.19 | 9.4 dB   |
| Peaking | 5678 Hz  | 3.22 | -11.8 dB |
| Peaking | 8786 Hz  | 3.95 | -9.9 dB  |
| Peaking | 90 Hz    | 9.76 | 3.0 dB   |
| Peaking | 1176 Hz  | 5.09 | 1.3 dB   |
| Peaking | 2481 Hz  | 2.09 | -2.4 dB  |
| Peaking | 3573 Hz  | 6.04 | 3.5 dB   |
| Peaking | 19416 Hz | 1.55 | -8.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20770%20600%20Ohm/Beyerdynamic%20DT%20770%20600%20Ohm.png)