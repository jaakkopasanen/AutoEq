# Meze Empyrean

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 0.0; 23 0.4; 25 0.4; 28 0.3; 31 0.1; 34 0.0; 37 -0.1; 41 -0.1; 45 -0.1; 49 -0.2; 54 -0.3; 60 -0.5; 66 -0.7; 72 -1.0; 79 -1.1; 87 -1.5; 96 -1.9; 106 -2.2; 116 -2.6; 128 -2.9; 141 -3.2; 155 -3.4; 170 -3.4; 187 -3.3; 206 -2.8; 227 -2.0; 249 -2.0; 274 -2.5; 302 -2.4; 332 -2.1; 365 -1.8; 402 -2.0; 442 -2.0; 486 -0.4; 535 0.2; 588 -0.6; 647 -1.0; 712 -0.8; 783 -0.5; 861 -0.8; 947 -0.0; 1042 -0.1; 1146 0.3; 1261 1.3; 1387 2.1; 1526 2.6; 1678 3.5; 1846 4.3; 2031 5.1; 2234 4.8; 2457 4.2; 2703 4.1; 2973 3.6; 3270 2.3; 3597 0.7; 3957 0.1; 4353 0.5; 4788 1.2; 5267 2.0; 5793 3.6; 6373 4.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.5; 12418 -1.1; 13660 0.0; 15026 -2.1; 16529 -4.6; 18182 -6.5; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Empyrean GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Empyrean ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 147 Hz   | 1.14 | -2.6 dB |
| Peaking | 311 Hz   | 0.69 | -1.3 dB |
| Peaking | 598 Hz   | 0.07 | -0.3 dB |
| Peaking | 2136 Hz  | 1.47 | 5.4 dB  |
| Peaking | 6216 Hz  | 3.11 | 3.5 dB  |
| Peaking | 310 Hz   | 4.35 | -0.2 dB |
| Peaking | 1499 Hz  | 4.17 | 0.5 dB  |
| Peaking | 13787 Hz | 4.8  | 2.1 dB  |
| Peaking | 19242 Hz | 0.8  | -6.3 dB |
| Peaking | 20053 Hz | 2.61 | -7.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%20Empyrean/Meze%20Empyrean.png)