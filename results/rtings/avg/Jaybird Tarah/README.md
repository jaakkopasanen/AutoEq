# Jaybird Tarah
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 0.0; 23 0.3; 25 0.3; 28 0.3; 31 0.3; 34 0.3; 37 0.3; 41 0.3; 45 0.3; 49 0.2; 54 0.1; 60 -0.2; 66 -0.6; 72 -0.9; 79 -1.2; 87 -1.5; 96 -1.9; 106 -2.5; 116 -3.2; 128 -4.1; 141 -4.7; 155 -5.0; 170 -5.1; 187 -5.0; 206 -4.8; 227 -4.6; 249 -4.1; 274 -3.7; 302 -3.2; 332 -2.7; 365 -2.2; 402 -1.7; 442 -1.1; 486 -0.6; 535 0.0; 588 0.6; 647 1.1; 712 1.7; 783 1.9; 861 1.8; 947 0.9; 1042 -0.6; 1146 -1.8; 1261 -2.3; 1387 -2.7; 1526 -3.1; 1678 -3.4; 1846 -3.8; 2031 -4.6; 2234 -5.1; 2457 -5.5; 2703 -5.3; 2973 -3.9; 3270 -2.3; 3597 -1.2; 3957 -0.8; 4353 -1.1; 4788 -1.2; 5267 -2.8; 5793 -5.4; 6373 -11.6; 7010 -8.6; 7711 -2.5; 8482 -0.6; 9330 -4.9; 10263 -7.6; 11289 -3.4; 12418 0.0; 13660 -0.5; 15026 -4.0; 16529 -2.4; 18182 0.0; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Tarah GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Tarah ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 180 Hz   | 1.03 | -5.5 dB  |
| Peaking | 2282 Hz  | 1.63 | -5.6 dB  |
| Peaking | 6516 Hz  | 5.46 | -12.4 dB |
| Peaking | 10282 Hz | 5.4  | -7.8 dB  |
| Peaking | 23224 Hz | 0.16 | -3.7 dB  |
| Peaking | 803 Hz   | 2.21 | 3.2 dB   |
| Peaking | 1259 Hz  | 2.13 | -1.8 dB  |
| Peaking | 3890 Hz  | 5.89 | 1.0 dB   |
| Peaking | 15577 Hz | 2.94 | -6.0 dB  |
| Peaking | 16935 Hz | 0.76 | 2.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Tarah/Jaybird%20Tarah.png)