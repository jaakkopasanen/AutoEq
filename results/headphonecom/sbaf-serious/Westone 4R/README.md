# Westone 4R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.2; 28 -0.3; 31 -0.8; 34 -1.2; 37 -1.5; 41 -1.9; 45 -2.3; 49 -2.6; 54 -3.1; 60 -3.5; 66 -4.0; 72 -4.3; 79 -4.8; 87 -5.1; 96 -5.4; 106 -5.6; 116 -5.9; 128 -6.2; 141 -6.5; 155 -6.7; 170 -6.9; 187 -6.9; 206 -6.9; 227 -6.8; 249 -6.7; 274 -6.5; 302 -6.2; 332 -5.8; 365 -5.3; 402 -4.9; 442 -4.4; 486 -3.9; 535 -3.3; 588 -2.5; 647 -1.8; 712 -1.0; 783 -0.4; 861 0.1; 947 0.2; 1042 -0.0; 1146 -0.4; 1261 -0.8; 1387 -1.2; 1526 -1.3; 1678 -1.1; 1846 -0.4; 2031 0.7; 2234 1.8; 2457 3.0; 2703 3.8; 2973 5.1; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.2; 9330 -6.4; 10263 -8.6; 11289 -3.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone 4R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone 4R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 117 Hz   | 0.52 | -4.3 dB  |
| Peaking | 331 Hz   | 0.53 | -5.4 dB  |
| Peaking | 1686 Hz  | 0.96 | -8.6 dB  |
| Peaking | 2898 Hz  | 0.29 | 9.2 dB   |
| Peaking | 9943 Hz  | 2.54 | -13.2 dB |
| Peaking | 20 Hz    | 2.07 | 1.7 dB   |
| Peaking | 862 Hz   | 3.64 | 0.6 dB   |
| Peaking | 6308 Hz  | 5.24 | 1.4 dB   |
| Peaking | 7307 Hz  | 6.38 | -1.9 dB  |
| Peaking | 11910 Hz | 9.93 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%204R/Westone%204R.png)