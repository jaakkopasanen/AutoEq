# Jabra Elite 65t

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.2; 31 4.3; 34 3.5; 37 2.8; 41 2.1; 45 1.6; 49 1.3; 54 1.0; 60 0.5; 66 0.0; 72 -0.3; 79 -0.6; 87 -0.9; 96 -1.3; 106 -1.9; 116 -2.4; 128 -3.0; 141 -3.4; 155 -3.6; 170 -3.7; 187 -3.9; 206 -4.1; 227 -4.1; 249 -3.8; 274 -3.3; 302 -2.9; 332 -2.5; 365 -2.2; 402 -1.7; 442 -1.2; 486 -0.6; 535 -0.1; 588 0.4; 647 1.1; 712 1.6; 783 1.5; 861 1.0; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.5; 1387 -2.2; 1526 -2.8; 1678 -3.0; 1846 -3.0; 2031 -2.9; 2234 -2.3; 2457 -1.4; 2703 -0.4; 2973 0.8; 3270 1.9; 3597 2.3; 3957 0.9; 4353 -1.3; 4788 -1.5; 5267 0.3; 5793 2.8; 6373 4.1; 7010 2.5; 7711 0.3; 8482 -3.6; 9330 -8.3; 10263 -9.7; 11289 -5.3; 12418 -0.1; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65t GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65t ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.07 | 6.2 dB   |
| Peaking | 190 Hz   | 0.92 | -4.4 dB  |
| Peaking | 1774 Hz  | 2.57 | -3.5 dB  |
| Peaking | 6526 Hz  | 3.72 | 5.5 dB   |
| Peaking | 9925 Hz  | 3.39 | -11.1 dB |
| Peaking | 733 Hz   | 2.83 | 2.4 dB   |
| Peaking | 2746 Hz  | 1.16 | -1.9 dB  |
| Peaking | 3474 Hz  | 1.9  | 4.4 dB   |
| Peaking | 4502 Hz  | 4.28 | -3.4 dB  |
| Peaking | 12707 Hz | 6.21 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jabra%20Elite%2065t/Jabra%20Elite%2065t.png)