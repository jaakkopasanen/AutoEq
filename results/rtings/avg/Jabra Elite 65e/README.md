# Jabra Elite 65e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.2dB
GraphicEQ: 21 -7.5; 23 -7.8; 25 -8.0; 28 -8.2; 31 -8.4; 34 -8.4; 37 -8.5; 41 -8.5; 45 -8.4; 49 -8.3; 54 -8.2; 60 -8.0; 66 -8.1; 72 -7.9; 79 -7.7; 87 -7.7; 96 -7.4; 106 -7.2; 116 -6.8; 128 -6.7; 141 -6.3; 155 -5.8; 170 -5.5; 187 -5.0; 206 -4.6; 227 -4.4; 249 -4.2; 274 -4.0; 302 -3.8; 332 -3.8; 365 -3.7; 402 -3.6; 442 -3.3; 486 -3.0; 535 -2.5; 588 -2.0; 647 -1.5; 712 -1.0; 783 -0.5; 861 -0.2; 947 -0.0; 1042 0.0; 1146 0.1; 1261 -0.0; 1387 -0.9; 1526 -2.2; 1678 -3.2; 1846 -3.5; 2031 -3.2; 2234 -2.2; 2457 -1.0; 2703 -0.5; 2973 -0.8; 3270 -1.8; 3597 -3.0; 3957 -4.4; 4353 -5.4; 4788 -2.4; 5267 -2.8; 5793 -2.4; 6373 -5.1; 7010 -8.1; 7711 -6.2; 8482 -4.9; 9330 -8.5; 10263 -12.8; 11289 -11.8; 12418 -8.8; 13660 -7.7; 15026 -8.3; 16529 -11.0; 18182 -12.5; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.13 | -8.2 dB  |
| Peaking | 1831 Hz  | 3.95 | -3.1 dB  |
| Peaking | 6743 Hz  | 0.71 | -3.6 dB  |
| Peaking | 10602 Hz | 3.02 | -8.7 dB  |
| Peaking | 18112 Hz | 0.81 | -12.2 dB |
| Peaking | 1027 Hz  | 3.15 | 1.1 dB   |
| Peaking | 2806 Hz  | 6.84 | 1.3 dB   |
| Peaking | 4159 Hz  | 5.11 | -3.6 dB  |
| Peaking | 6252 Hz  | 1.93 | 4.0 dB   |
| Peaking | 6851 Hz  | 5.47 | -6.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jabra%20Elite%2065e/Jabra%20Elite%2065e.png)