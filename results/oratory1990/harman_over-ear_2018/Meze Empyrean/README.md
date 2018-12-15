# Meze Empyrean

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.8; 41 5.7; 45 5.5; 49 5.2; 54 4.9; 60 4.5; 66 4.0; 72 3.5; 79 3.0; 87 2.3; 96 1.5; 106 0.6; 116 -0.2; 128 -1.0; 141 -1.8; 155 -2.4; 170 -2.8; 187 -3.0; 206 -2.7; 227 -2.0; 249 -2.0; 274 -2.5; 302 -2.4; 332 -2.1; 365 -1.8; 402 -2.0; 442 -2.0; 486 -0.4; 535 0.2; 588 -0.6; 647 -1.0; 712 -0.8; 783 -0.5; 861 -0.8; 947 -0.0; 1042 -0.1; 1146 0.3; 1261 1.3; 1387 2.1; 1526 2.6; 1678 3.5; 1846 4.3; 2031 5.1; 2234 4.8; 2457 4.2; 2703 4.1; 2973 3.6; 3270 2.3; 3597 0.7; 3957 0.1; 4353 0.5; 4788 1.2; 5267 2.0; 5793 3.6; 6373 4.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.5; 12418 -1.1; 13660 0.0; 15026 -2.1; 16529 -4.6; 18182 -6.5; 20000 -14.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze Empyrean GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Empyrean ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.23 | 7.5 dB   |
| Peaking | 164 Hz   | 0.52 | -7.3 dB  |
| Peaking | 2143 Hz  | 1.51 | 5.3 dB   |
| Peaking | 6272 Hz  | 4.03 | 4.6 dB   |
| Peaking | 20033 Hz | 1.17 | -13.3 dB |
| Peaking | 407 Hz   | 4.22 | -0.3 dB  |
| Peaking | 2997 Hz  | 6.21 | 1.3 dB   |
| Peaking | 3855 Hz  | 4.59 | -1.3 dB  |
| Peaking | 13713 Hz | 7.07 | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%20Empyrean/Meze%20Empyrean.png)