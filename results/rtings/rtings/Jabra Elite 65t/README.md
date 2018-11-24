# Jabra Elite 65t

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.1; 31 4.2; 34 3.5; 37 2.9; 41 2.3; 45 1.9; 49 1.6; 54 1.3; 60 0.7; 66 0.2; 72 -0.3; 79 -0.8; 87 -1.3; 96 -1.7; 106 -2.4; 116 -2.9; 128 -3.5; 141 -3.9; 155 -4.2; 170 -4.4; 187 -4.5; 206 -4.6; 227 -4.6; 249 -4.3; 274 -4.0; 302 -3.7; 332 -3.5; 365 -3.2; 402 -2.8; 442 -2.3; 486 -1.8; 535 -1.3; 588 -0.7; 647 0.1; 712 0.7; 783 1.0; 861 0.8; 947 0.4; 1042 -0.4; 1146 -1.1; 1261 -1.7; 1387 -2.2; 1526 -2.4; 1678 -2.7; 1846 -3.0; 2031 -3.3; 2234 -2.8; 2457 -1.9; 2703 -1.0; 2973 -0.3; 3270 0.1; 3597 0.1; 3957 -0.3; 4353 -1.3; 4788 -1.3; 5267 -0.2; 5793 1.4; 6373 1.6; 7010 2.1; 7711 0.2; 8482 -3.9; 9330 -9.8; 10263 -13.1; 11289 -9.8; 12418 -3.3; 13660 -0.0
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
| Peaking | 22 Hz    | 0.75 | 6.2 dB   |
| Peaking | 193 Hz   | 0.73 | -5.0 dB  |
| Peaking | 1894 Hz  | 2.1  | -3.4 dB  |
| Peaking | 6964 Hz  | 2.98 | 4.4 dB   |
| Peaking | 10198 Hz | 2.95 | -14.7 dB |
| Peaking | 814 Hz   | 2.7  | 2.2 dB   |
| Peaking | 1396 Hz  | 1.51 | -1.1 dB  |
| Peaking | 1750 Hz  | 4.5  | 1.0 dB   |
| Peaking | 11402 Hz | 5.89 | -2.8 dB  |
| Peaking | 13384 Hz | 2.33 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jabra%20Elite%2065t/Jabra%20Elite%2065t.png)