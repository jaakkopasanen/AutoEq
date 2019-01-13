# Beyerdynamic T70p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.9; 25 0.7; 28 0.5; 31 0.4; 34 0.3; 37 0.1; 41 0.0; 45 -0.0; 49 -0.1; 54 -0.2; 60 -0.4; 66 -0.5; 72 -0.7; 79 -0.7; 87 -0.9; 96 -0.9; 106 -0.9; 116 -0.9; 128 -1.4; 141 -2.2; 155 -2.3; 170 -1.0; 187 -1.5; 206 -1.2; 227 -0.9; 249 -0.4; 274 -0.2; 302 -0.1; 332 -0.2; 365 -0.3; 402 -0.6; 442 -0.8; 486 -0.7; 535 0.5; 588 0.5; 647 0.3; 712 0.2; 783 0.2; 861 0.1; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.3; 1387 -0.8; 1526 -1.4; 1678 -1.5; 1846 -0.6; 2031 2.2; 2234 4.3; 2457 4.8; 2703 4.1; 2973 3.8; 3270 3.5; 3597 3.5; 3957 6.0; 4353 2.9; 4788 4.2; 5267 6.0; 5793 6.0; 6373 5.2; 7010 -2.0; 7711 -7.0; 8482 -9.8; 9330 -10.1; 10263 -7.2; 11289 -0.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 149 Hz   | 1.27 | -1.8 dB  |
| Peaking | 2462 Hz  | 4.01 | 4.7 dB   |
| Peaking | 3850 Hz  | 2.66 | 4.1 dB   |
| Peaking | 5875 Hz  | 2.8  | 8.6 dB   |
| Peaking | 8679 Hz  | 2.4  | -12.7 dB |
| Peaking | 22 Hz    | 1.55 | 1.0 dB   |
| Peaking | 1620 Hz  | 4.71 | -2.4 dB  |
| Peaking | 10090 Hz | 5.28 | -4.3 dB  |
| Peaking | 11530 Hz | 2.38 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T70p/Beyerdynamic%20T70p.png)