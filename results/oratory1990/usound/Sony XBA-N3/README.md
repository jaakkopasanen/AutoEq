# Sony XBA-N3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 -3.8; 23 -4.0; 25 -4.2; 28 -4.4; 31 -4.5; 34 -4.5; 37 -4.5; 41 -4.6; 45 -4.6; 49 -4.5; 54 -4.5; 60 -4.5; 66 -4.5; 72 -4.5; 79 -4.4; 87 -4.4; 96 -4.2; 106 -3.9; 116 -4.2; 128 -4.6; 141 -4.6; 155 -4.4; 170 -4.0; 187 -3.7; 206 -3.3; 227 -2.9; 249 -2.5; 274 -2.1; 302 -1.7; 332 -1.4; 365 -1.0; 402 -0.7; 442 -0.5; 486 -0.2; 535 -0.0; 588 0.2; 647 0.3; 712 0.5; 783 0.6; 861 0.5; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.3; 1387 -1.5; 1526 -0.5; 1678 0.2; 1846 -0.1; 2031 -0.0; 2234 0.3; 2457 0.8; 2703 1.7; 2973 2.4; 3270 2.5; 3597 1.1; 3957 0.2; 4353 2.0; 4788 1.3; 5267 1.8; 5793 3.0; 6373 2.3; 7010 -1.0; 7711 -3.2; 8482 -3.3; 9330 -2.0; 10263 -1.1; 11289 -1.2; 12418 -0.3; 13660 -0.1; 15026 -2.8; 16529 -4.5; 18182 -1.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-N3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.34 | -4.5 dB |
| Peaking | 163 Hz   | 1.05 | -2.7 dB |
| Peaking | 6537 Hz  | 1.08 | 5.6 dB  |
| Peaking | 7958 Hz  | 1.95 | -8.0 dB |
| Peaking | 16334 Hz | 2.55 | -5.0 dB |
| Peaking | 762 Hz   | 1.63 | 0.9 dB  |
| Peaking | 1312 Hz  | 3.14 | -1.8 dB |
| Peaking | 3154 Hz  | 3.6  | 2.4 dB  |
| Peaking | 3802 Hz  | 4.28 | -1.9 dB |
| Peaking | 13511 Hz | 8.16 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20XBA-N3/Sony%20XBA-N3.png)