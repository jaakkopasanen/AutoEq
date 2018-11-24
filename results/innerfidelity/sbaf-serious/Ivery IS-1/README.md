# Ivery IS-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.9; 23 -11.0; 25 -11.1; 28 -11.1; 31 -11.2; 34 -11.3; 37 -11.3; 41 -11.5; 45 -11.6; 49 -11.7; 54 -11.8; 60 -12.0; 66 -12.2; 72 -12.4; 79 -12.6; 87 -12.9; 96 -13.1; 106 -13.1; 116 -13.0; 128 -13.1; 141 -13.0; 155 -12.9; 170 -12.7; 187 -12.4; 206 -12.0; 227 -11.4; 249 -11.0; 274 -10.3; 302 -9.8; 332 -9.1; 365 -8.4; 402 -7.6; 442 -6.7; 486 -6.0; 535 -5.2; 588 -4.0; 647 -3.3; 712 -2.3; 783 -1.2; 861 -1.0; 947 -0.6; 1042 0.9; 1146 1.4; 1261 1.5; 1387 1.7; 1526 2.1; 1678 2.8; 1846 3.9; 2031 5.5; 2234 6.0; 2457 6.0; 2703 5.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.5; 4353 2.7; 4788 1.9; 5267 2.3; 5793 2.1; 6373 -0.8; 7010 -6.4; 7711 -8.4; 8482 -4.4; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 -0.9; 13660 -1.8; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ivery IS-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ivery IS-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.13 | -8.8 dB  |
| Peaking | 364 Hz   | 0.22 | -10.3 dB |
| Peaking | 1658 Hz  | 0.27 | 9.5 dB   |
| Peaking | 7532 Hz  | 3.11 | -12.2 dB |
| Peaking | 22 Hz    | 1.13 | -1.3 dB  |
| Peaking | 1534 Hz  | 2.48 | -2.3 dB  |
| Peaking | 2801 Hz  | 0.52 | 1.3 dB   |
| Peaking | 4613 Hz  | 5.38 | -3.1 dB  |
| Peaking | 13306 Hz | 4.51 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ivery%20IS-1/Ivery%20IS-1.png)