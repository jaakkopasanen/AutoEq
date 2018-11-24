# Jaybird Tarah

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 0.0; 23 0.3; 25 0.3; 28 0.3; 31 0.3; 34 0.3; 37 0.3; 41 0.3; 45 0.3; 49 0.2; 54 0.1; 60 -0.2; 66 -0.6; 72 -0.9; 79 -1.2; 87 -1.5; 96 -1.9; 106 -2.5; 116 -3.2; 128 -4.1; 141 -4.7; 155 -5.0; 170 -5.1; 187 -5.0; 206 -4.8; 227 -4.6; 249 -4.1; 274 -3.7; 302 -3.2; 332 -2.7; 365 -2.2; 402 -1.7; 442 -1.1; 486 -0.6; 535 0.0; 588 0.6; 647 1.1; 712 1.7; 783 1.9; 861 1.8; 947 0.9; 1042 -0.6; 1146 -1.8; 1261 -2.3; 1387 -2.7; 1526 -3.1; 1678 -3.4; 1846 -3.8; 2031 -4.6; 2234 -5.1; 2457 -5.5; 2703 -5.1; 2973 -3.4; 3270 -1.6; 3597 -0.2; 3957 0.4; 4353 0.2; 4788 0.6; 5267 -0.2; 5793 -2.9; 6373 -10.4; 7010 -7.7; 7711 -1.1; 8482 -0.2; 9330 -6.2; 10263 -9.4; 11289 -2.7; 12418 0.0; 13660 0.0; 15026 -1.4; 16529 -0.2; 18182 0.0
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
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 186 Hz   | 0.88 | -5.3 dB  |
| Peaking | 758 Hz   | 2.47 | 3.1 dB   |
| Peaking | 2134 Hz  | 1.46 | -5.4 dB  |
| Peaking | 6651 Hz  | 5.8  | -11.4 dB |
| Peaking | 21835 Hz | 1.83 | -5.5 dB  |
| Peaking | 2699 Hz  | 5.56 | -1.9 dB  |
| Peaking | 3018 Hz  | 3.24 | -0.2 dB  |
| Peaking | 4209 Hz  | 1.97 | 2.2 dB   |
| Peaking | 8242 Hz  | 6.39 | 3.5 dB   |
| Peaking | 10089 Hz | 4.84 | -10.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jaybird%20Tarah/Jaybird%20Tarah.png)