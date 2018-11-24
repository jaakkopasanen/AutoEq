# Pioneer SE Master 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 0.0; 23 2.1; 25 1.5; 28 0.9; 31 0.4; 34 0.2; 37 0.0; 41 -0.4; 45 -1.1; 49 -1.8; 54 -2.6; 60 -3.3; 66 -3.9; 72 -4.5; 79 -5.0; 87 -5.5; 96 -6.0; 106 -6.4; 116 -6.6; 128 -6.9; 141 -7.0; 155 -7.1; 170 -6.9; 187 -6.9; 206 -6.7; 227 -6.3; 249 -6.0; 274 -5.6; 302 -5.1; 332 -4.7; 365 -4.2; 402 -3.8; 442 -3.2; 486 -2.9; 535 -2.4; 588 -1.5; 647 -1.3; 712 -1.1; 783 -0.6; 861 -0.5; 947 -0.2; 1042 0.2; 1146 1.1; 1261 2.1; 1387 2.2; 1526 1.7; 1678 1.4; 1846 0.5; 2031 -1.0; 2234 -2.2; 2457 -2.3; 2703 -2.7; 2973 -2.7; 3270 -1.1; 3597 0.5; 3957 0.7; 4353 -1.4; 4788 -3.2; 5267 -4.3; 5793 -9.4; 6373 -10.2; 7010 -4.3; 7711 -2.8; 8482 -1.9; 9330 -0.9; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.9; 18182 -9.3; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE Master 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE Master 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.68 | 4.1 dB   |
| Peaking | 122 Hz   | 0.6  | -6.4 dB  |
| Peaking | 278 Hz   | 1.02 | -3.0 dB  |
| Peaking | 2687 Hz  | 4.62 | -2.9 dB  |
| Peaking | 6112 Hz  | 4.37 | -12.2 dB |
| Peaking | 486 Hz   | 3.94 | -0.7 dB  |
| Peaking | 1401 Hz  | 2.27 | 2.8 dB   |
| Peaking | 2202 Hz  | 5.21 | -1.7 dB  |
| Peaking | 3786 Hz  | 8.18 | 2.1 dB   |
| Peaking | 19117 Hz | 1.87 | -12.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE%20Master%201/Pioneer%20SE%20Master%201.png)