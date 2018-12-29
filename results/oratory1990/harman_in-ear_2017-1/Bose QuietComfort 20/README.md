# Bose QuietComfort 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 21 -0.9; 23 -2.1; 25 -3.0; 28 -4.0; 31 -4.4; 34 -4.6; 37 -4.6; 41 -4.6; 45 -4.4; 49 -4.3; 54 -4.2; 60 -4.2; 66 -4.3; 72 -4.5; 79 -4.9; 87 -5.3; 96 -5.7; 106 -6.0; 116 -6.0; 128 -5.9; 141 -5.5; 155 -5.2; 170 -5.1; 187 -5.0; 206 -5.0; 227 -5.0; 249 -5.0; 274 -5.0; 302 -5.0; 332 -4.8; 365 -4.7; 402 -4.8; 442 -4.9; 486 -4.7; 535 -3.8; 588 -2.4; 647 -1.4; 712 -0.7; 783 0.1; 861 0.8; 947 0.5; 1042 -0.5; 1146 -1.5; 1261 -2.3; 1387 -2.8; 1526 -5.2; 1678 -7.2; 1846 -7.2; 2031 -5.5; 2234 -3.8; 2457 -3.0; 2703 -2.2; 2973 -1.8; 3270 -1.8; 3597 -2.5; 3957 -4.0; 4353 -4.0; 4788 -1.6; 5267 2.2; 5793 4.5; 6373 4.1; 7010 -1.5; 7711 -4.2; 8482 -1.3; 9330 -0.6; 10263 -2.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -6.8; 16529 -11.1; 18182 -10.5; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 1.35 | -3.4 dB  |
| Peaking | 127 Hz   | 0.54 | -5.6 dB  |
| Peaking | 401 Hz   | 1.75 | -3.4 dB  |
| Peaking | 1820 Hz  | 2.26 | -7.4 dB  |
| Peaking | 17820 Hz | 1.35 | -12.5 dB |
| Peaking | 880 Hz   | 3.98 | 2.4 dB   |
| Peaking | 4276 Hz  | 2.97 | -5.5 dB  |
| Peaking | 6026 Hz  | 2.46 | 7.6 dB   |
| Peaking | 7460 Hz  | 4.64 | -6.7 dB  |
| Peaking | 13085 Hz | 4.55 | 3.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)