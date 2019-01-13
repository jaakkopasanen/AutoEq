# Monster Solo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.2; 23 -4.5; 25 -4.7; 28 -5.1; 31 -5.4; 34 -5.7; 37 -5.9; 41 -6.3; 45 -6.5; 49 -6.7; 54 -7.0; 60 -7.5; 66 -8.0; 72 -8.4; 79 -8.7; 87 -8.7; 96 -8.4; 106 -8.0; 116 -8.5; 128 -9.7; 141 -10.7; 155 -10.4; 170 -9.6; 187 -9.5; 206 -8.6; 227 -7.3; 249 -5.9; 274 -4.5; 302 -3.8; 332 -3.0; 365 -2.1; 402 -1.0; 442 -0.0; 486 0.6; 535 0.8; 588 0.8; 647 0.6; 712 0.2; 783 -0.1; 861 -0.3; 947 -0.2; 1042 0.2; 1146 0.9; 1261 1.5; 1387 1.9; 1526 2.0; 1678 2.0; 1846 2.2; 2031 2.4; 2234 2.6; 2457 2.8; 2703 3.0; 2973 3.5; 3270 3.5; 3597 2.9; 3957 1.5; 4353 0.2; 4788 1.4; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Solo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Solo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.18 | -6.8 dB |
| Peaking | 67 Hz   | 0.55 | -7.0 dB |
| Peaking | 171 Hz  | 1.24 | -7.5 dB |
| Peaking | 3422 Hz | 0.44 | 3.2 dB  |
| Peaking | 521 Hz  | 2.85 | 1.7 dB  |
| Peaking | 912 Hz  | 3.75 | -1.2 dB |
| Peaking | 4482 Hz | 3.85 | -5.9 dB |
| Peaking | 5840 Hz | 1.67 | 7.7 dB  |
| Peaking | 7593 Hz | 1.3  | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Solo/Monster%20Solo.png)