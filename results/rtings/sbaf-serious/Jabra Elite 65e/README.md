# Jabra Elite 65e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.7dB
GraphicEQ: 21 -7.1; 23 -7.4; 25 -7.7; 28 -8.0; 31 -8.3; 34 -8.5; 37 -8.6; 41 -8.7; 45 -8.7; 49 -8.7; 54 -8.5; 60 -8.3; 66 -8.2; 72 -7.9; 79 -7.5; 87 -7.4; 96 -6.9; 106 -6.7; 116 -6.3; 128 -6.1; 141 -5.7; 155 -5.2; 170 -4.9; 187 -4.4; 206 -4.1; 227 -3.9; 249 -3.6; 274 -3.3; 302 -3.0; 332 -2.9; 365 -2.6; 402 -2.5; 442 -2.2; 486 -1.8; 535 -1.3; 588 -1.0; 647 -0.5; 712 -0.1; 783 0.0; 861 0.0; 947 0.0; 1042 0.1; 1146 0.3; 1261 0.2; 1387 -0.9; 1526 -2.6; 1678 -3.5; 1846 -3.5; 2031 -2.7; 2234 -1.7; 2457 -0.6; 2703 0.4; 2973 0.8; 3270 0.8; 3597 0.2; 3957 -2.0; 4353 -4.1; 4788 -0.8; 5267 0.2; 5793 1.5; 6373 -1.3; 7010 -4.9; 7711 -4.6; 8482 -5.5; 9330 -9.7; 10263 -11.6; 11289 -6.5; 12418 -1.0; 13660 -0.6; 15026 -2.4; 16529 -4.6; 18182 -4.9; 20000 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite 65e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-17**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite 65e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.21 | -8.4 dB  |
| Peaking | 1785 Hz  | 3.74 | -3.9 dB  |
| Peaking | 9860 Hz  | 2.75 | -12.0 dB |
| Peaking | 17625 Hz | 2.18 | -5.6 dB  |
| Peaking | 3209 Hz  | 3.39 | 1.6 dB   |
| Peaking | 4272 Hz  | 6.63 | -4.4 dB  |
| Peaking | 6013 Hz  | 3.81 | 4.5 dB   |
| Peaking | 6829 Hz  | 4.71 | -5.0 dB  |
| Peaking | 12908 Hz | 5.93 | 2.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Jabra%20Elite%2065e/Jabra%20Elite%2065e.png)