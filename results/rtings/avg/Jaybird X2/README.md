# Jaybird X2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.8; 28 1.8; 31 1.8; 34 1.8; 37 1.7; 41 1.7; 45 1.7; 49 1.6; 54 1.4; 60 1.0; 66 0.6; 72 0.3; 79 -0.1; 87 -0.6; 96 -1.1; 106 -1.7; 116 -2.2; 128 -2.7; 141 -3.0; 155 -3.3; 170 -3.6; 187 -3.7; 206 -3.6; 227 -3.5; 249 -3.3; 274 -3.0; 302 -2.5; 332 -2.0; 365 -1.6; 402 -1.1; 442 -0.6; 486 -0.1; 535 0.5; 588 1.1; 647 1.7; 712 2.0; 783 1.9; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.3; 1387 -1.4; 1526 -1.5; 1678 -1.6; 1846 -1.6; 2031 -1.4; 2234 -0.9; 2457 -0.4; 2703 -0.4; 2973 -0.6; 3270 -0.4; 3597 -0.4; 3957 -0.4; 4353 -0.3; 4788 0.5; 5267 1.0; 5793 1.8; 6373 1.3; 7010 0.9; 7711 -1.7; 8482 -3.7; 9330 -4.3; 10263 -6.4; 11289 -9.6; 12418 -9.3; 13660 -5.0; 15026 -2.7; 16529 -6.2; 18182 -10.9; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 57 Hz    | 0.29 | 2.8 dB   |
| Peaking | 167 Hz   | 0.58 | -5.4 dB  |
| Peaking | 673 Hz   | 2.44 | 3.0 dB   |
| Peaking | 11547 Hz | 2.58 | -9.6 dB  |
| Peaking | 19052 Hz | 1.32 | -12.5 dB |
| Peaking | 848 Hz   | 3.99 | 1.2 dB   |
| Peaking | 1573 Hz  | 1.2  | -1.7 dB  |
| Peaking | 6351 Hz  | 2.28 | 3.0 dB   |
| Peaking | 8437 Hz  | 3.42 | -2.4 dB  |
| Peaking | 14932 Hz | 7.18 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X2/Jaybird%20X2.png)