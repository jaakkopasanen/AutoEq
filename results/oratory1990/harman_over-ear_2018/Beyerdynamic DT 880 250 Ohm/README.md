# Beyerdynamic DT880 250 Ohm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.6; 45 5.4; 49 5.2; 54 5.0; 60 4.7; 66 4.4; 72 4.3; 79 4.5; 87 4.0; 96 2.8; 106 2.1; 116 1.6; 128 1.2; 141 0.8; 155 0.5; 170 0.3; 187 0.1; 206 -0.1; 227 -0.2; 249 -0.2; 274 -0.1; 302 -0.0; 332 0.1; 365 0.2; 402 0.3; 442 0.3; 486 0.6; 535 0.8; 588 0.6; 647 0.7; 712 0.8; 783 0.8; 861 0.3; 947 0.0; 1042 0.0; 1146 0.2; 1261 0.2; 1387 0.1; 1526 0.1; 1678 -0.1; 1846 -0.2; 2031 -0.2; 2234 -0.3; 2457 -0.8; 2703 -1.7; 2973 -2.0; 3270 -1.4; 3597 -0.7; 3957 -1.1; 4353 -0.7; 4788 -0.1; 5267 -2.0; 5793 -6.4; 6373 -5.3; 7010 -2.1; 7711 -1.5; 8482 -1.2; 9330 -0.0; 10263 0.0; 11289 -1.6; 12418 -2.3; 13660 -0.5; 15026 -0.9; 16529 -5.4; 18182 -9.2; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT880 250 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT880 250 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.49 | 6.4 dB   |
| Peaking | 2906 Hz  | 2.63 | -2.3 dB  |
| Peaking | 6008 Hz  | 0.12 | 0.5 dB   |
| Peaking | 6033 Hz  | 4.59 | -7.3 dB  |
| Peaking | 19301 Hz | 1.13 | -11.8 dB |
| Peaking | 81 Hz    | 4.49 | 1.5 dB   |
| Peaking | 194 Hz   | 1.42 | -0.9 dB  |
| Peaking | 12182 Hz | 5.22 | -2.1 dB  |
| Peaking | 14530 Hz | 2.92 | 2.5 dB   |
| Peaking | 17074 Hz | 3.62 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%20880%20250%20Ohm/Beyerdynamic%20DT880%20250%20Ohm.png)