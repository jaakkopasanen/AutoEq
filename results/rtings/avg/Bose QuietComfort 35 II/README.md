# Bose QuietComfort 35 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 21 -5.7; 23 -5.1; 25 -4.7; 28 -4.4; 31 -4.3; 34 -4.3; 37 -4.3; 41 -4.4; 45 -4.4; 49 -4.4; 54 -4.4; 60 -4.3; 66 -4.2; 72 -4.2; 79 -4.1; 87 -4.0; 96 -4.0; 106 -3.9; 116 -3.9; 128 -3.8; 141 -3.8; 155 -3.7; 170 -3.5; 187 -3.4; 206 -3.1; 227 -2.8; 249 -2.6; 274 -2.5; 302 -2.4; 332 -2.2; 365 -2.0; 402 -1.9; 442 -1.9; 486 -1.8; 535 -1.6; 588 -1.4; 647 -1.1; 712 -0.9; 783 -0.5; 861 -0.1; 947 -0.1; 1042 0.1; 1146 0.6; 1261 0.8; 1387 0.3; 1526 -0.3; 1678 -1.9; 1846 -3.8; 2031 -5.1; 2234 -4.5; 2457 -3.1; 2703 -2.2; 2973 -1.6; 3270 -0.1; 3597 -2.8; 3957 -4.8; 4353 -3.3; 4788 -1.5; 5267 1.6; 5793 -1.5; 6373 -6.2; 7010 -1.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.1; 12418 -4.3; 13660 -5.7; 15026 -5.2; 16529 -2.6; 18182 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 13 Hz    |  1    | -6.5 dB |
| Peaking | 81 Hz    |  0.25 | -4.0 dB |
| Peaking | 2159 Hz  |  2.62 | -5.0 dB |
| Peaking | 6290 Hz  |  9.19 | -6.6 dB |
| Peaking | 14232 Hz |  2.3  | -6.5 dB |
| Peaking | 1285 Hz  |  2.63 | 1.5 dB  |
| Peaking | 1865 Hz  |  5.7  | -1.4 dB |
| Peaking | 4045 Hz  |  4.22 | -5.1 dB |
| Peaking | 4565 Hz  |  0.4  | 0.7 dB  |
| Peaking | 5429 Hz  | 12.54 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2035%20II/Bose%20QuietComfort%2035%20II.png)