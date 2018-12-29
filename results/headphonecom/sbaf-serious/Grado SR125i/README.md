# Grado SR125i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.4; 60 4.2; 66 3.0; 72 2.0; 79 1.1; 87 0.2; 96 -0.4; 106 -0.9; 116 -1.1; 128 -1.1; 141 -1.0; 155 -1.0; 170 -0.9; 187 -0.7; 206 -0.5; 227 -0.3; 249 -0.0; 274 0.5; 302 0.5; 332 -0.4; 365 0.0; 402 0.2; 442 0.2; 486 0.4; 535 0.5; 588 0.5; 647 0.7; 712 0.7; 783 0.6; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -1.0; 1387 -2.0; 1526 -3.1; 1678 -4.1; 1846 -5.1; 2031 -5.7; 2234 -6.3; 2457 -5.3; 2703 -4.1; 2973 -2.7; 3270 -1.7; 3597 -1.6; 3957 -1.9; 4353 -2.2; 4788 -5.4; 5267 -5.7; 5793 -7.3; 6373 -6.2; 7010 -6.6; 7711 -6.1; 8482 -8.7; 9330 -10.3; 10263 -5.7; 11289 -0.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.6; 20000 -8.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR125i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR125i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 64 Hz    | 0.25 | 11.2 dB  |
| Peaking | 111 Hz   | 0.53 | -11.2 dB |
| Peaking | 2101 Hz  | 1.94 | -6.3 dB  |
| Peaking | 5978 Hz  | 2.05 | -6.4 dB  |
| Peaking | 9099 Hz  | 3.88 | -9.9 dB  |
| Peaking | 833 Hz   | 1.27 | 1.2 dB   |
| Peaking | 1577 Hz  | 0.15 | -0.6 dB  |
| Peaking | 3628 Hz  | 2.61 | 1.3 dB   |
| Peaking | 11926 Hz | 3.32 | 2.2 dB   |
| Peaking | 19906 Hz | 3.09 | -8.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR125i/Grado%20SR125i.png)