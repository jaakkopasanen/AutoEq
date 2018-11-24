# Jaybird Freedom 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 21 -7.3; 23 -7.5; 25 -7.6; 28 -7.8; 31 -7.9; 34 -8.0; 37 -8.1; 41 -8.2; 45 -8.2; 49 -8.3; 54 -8.4; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.3; 87 -9.4; 96 -9.6; 106 -9.8; 116 -10.0; 128 -10.1; 141 -10.1; 155 -10.2; 170 -10.5; 187 -10.1; 206 -9.6; 227 -9.0; 249 -8.3; 274 -7.6; 302 -6.8; 332 -6.0; 365 -5.2; 402 -4.4; 442 -3.6; 486 -2.8; 535 -2.0; 588 -1.1; 647 -0.2; 712 0.7; 783 1.1; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.2; 1261 -1.9; 1387 -2.2; 1526 -2.4; 1678 -2.4; 1846 -3.0; 2031 -3.9; 2234 -4.7; 2457 -5.5; 2703 -5.4; 2973 -3.6; 3270 -1.5; 3597 -0.4; 3957 0.0; 4353 -0.2; 4788 -0.3; 5267 -1.2; 5793 -3.2; 6373 -8.5; 7010 -11.9; 7711 -7.7; 8482 -2.5; 9330 -2.4; 10263 -7.2; 11289 -10.6; 12418 -8.7; 13660 -5.3; 15026 -6.1; 16529 -7.0; 18182 -3.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Freedom 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Freedom 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.25 | -7.6 dB  |
| Peaking | 151 Hz   | 0.77 | -5.2 dB  |
| Peaking | 259 Hz   | 1.14 | -3.4 dB  |
| Peaking | 6895 Hz  | 6.15 | -10.3 dB |
| Peaking | 12959 Hz | 0.72 | -7.9 dB  |
| Peaking | 794 Hz   | 2.58 | 2.8 dB   |
| Peaking | 2769 Hz  | 1.12 | -8.1 dB  |
| Peaking | 3645 Hz  | 1.45 | 6.5 dB   |
| Peaking | 9031 Hz  | 6.57 | 4.6 dB   |
| Peaking | 11189 Hz | 6.32 | -4.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Freedom%202/Jaybird%20Freedom%202.png)