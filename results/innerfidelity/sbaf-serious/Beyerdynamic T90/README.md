# Beyerdynamic T90

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 0.0; 23 3.9; 25 3.7; 28 3.3; 31 2.9; 34 2.7; 37 2.5; 41 2.3; 45 2.2; 49 2.0; 54 2.0; 60 2.4; 66 1.3; 72 0.4; 79 -0.3; 87 -0.8; 96 -1.4; 106 -2.0; 116 -2.3; 128 -2.8; 141 -3.1; 155 -3.3; 170 -3.3; 187 -3.6; 206 -3.7; 227 -3.7; 249 -3.7; 274 -3.5; 302 -3.5; 332 -3.3; 365 -3.0; 402 -2.7; 442 -2.4; 486 -2.2; 535 -1.7; 588 -1.0; 647 -0.5; 712 -0.2; 783 0.1; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.1; 1261 -0.3; 1387 -1.0; 1526 -1.8; 1678 -2.6; 1846 -2.9; 2031 -3.1; 2234 -3.2; 2457 -2.9; 2703 -3.5; 2973 -4.1; 3270 -4.1; 3597 -3.5; 3957 -3.6; 4353 -3.5; 4788 1.9; 5267 0.7; 5793 -0.2; 6373 -6.8; 7010 -9.0; 7711 -10.6; 8482 -12.1; 9330 -11.4; 10263 -8.0; 11289 -5.1; 12418 -4.0; 13660 -3.1; 15026 -3.1; 16529 -5.1; 18182 -6.4; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T90 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.22 | 4.1 dB   |
| Peaking | 189 Hz   | 0.57 | -4.4 dB  |
| Peaking | 2632 Hz  | 1.48 | -3.6 dB  |
| Peaking | 8613 Hz  | 2.03 | -12.8 dB |
| Peaking | 17915 Hz | 1.28 | -6.2 dB  |
| Peaking | 861 Hz   | 2.76 | 1.2 dB   |
| Peaking | 4307 Hz  | 3.23 | -5.0 dB  |
| Peaking | 4800 Hz  | 3.31 | 6.6 dB   |
| Peaking | 5932 Hz  | 4.34 | 2.7 dB   |
| Peaking | 6644 Hz  | 5.8  | -5.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T90/Beyerdynamic%20T90.png)