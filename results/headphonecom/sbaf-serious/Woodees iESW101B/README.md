# Woodees iESW101B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -9.4; 23 -9.3; 25 -9.3; 28 -9.2; 31 -9.1; 34 -9.0; 37 -8.9; 41 -8.8; 45 -8.7; 49 -8.7; 54 -8.6; 60 -8.5; 66 -8.5; 72 -8.4; 79 -8.3; 87 -8.2; 96 -8.0; 106 -7.8; 116 -7.5; 128 -7.2; 141 -6.9; 155 -6.6; 170 -6.2; 187 -5.8; 206 -5.2; 227 -4.7; 249 -4.1; 274 -3.5; 302 -2.8; 332 -2.2; 365 -1.4; 402 -0.8; 442 -0.1; 486 0.4; 535 0.9; 588 1.2; 647 1.4; 712 1.3; 783 1.1; 861 0.8; 947 0.4; 1042 -0.1; 1146 -0.6; 1261 -1.1; 1387 -1.9; 1526 -2.9; 1678 -3.6; 1846 -4.0; 2031 -4.7; 2234 -5.5; 2457 -6.6; 2703 -7.5; 2973 -5.6; 3270 -1.6; 3597 1.3; 3957 1.1; 4353 -1.2; 4788 -3.3; 5267 -6.2; 5793 -11.8; 6373 -5.6; 7010 -1.3; 7711 0.2; 8482 -0.7; 9330 -4.3; 10263 -4.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Woodees iESW101B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-16**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Woodees iESW101B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.28 | -9.1 dB  |
| Peaking | 145 Hz   | 0.92 | -3.8 dB  |
| Peaking | 2412 Hz  | 2.23 | -7.1 dB  |
| Peaking | 5780 Hz  | 5.77 | -12.1 dB |
| Peaking | 21594 Hz | 1.87 | -2.1 dB  |
| Peaking | 655 Hz   | 1.74 | 2.2 dB   |
| Peaking | 1592 Hz  | 3.93 | -1.9 dB  |
| Peaking | 2866 Hz  | 8.45 | -3.0 dB  |
| Peaking | 3687 Hz  | 4.97 | 4.0 dB   |
| Peaking | 9772 Hz  | 7.25 | -5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Woodees%20iESW101B/Woodees%20iESW101B.png)