# Adam SP-5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.2; 54 4.1; 60 3.1; 66 2.3; 72 1.8; 79 2.0; 87 2.1; 96 2.2; 106 2.1; 116 1.1; 128 0.5; 141 -0.4; 155 -0.7; 170 -0.6; 187 -0.1; 206 -0.2; 227 0.3; 249 1.1; 274 1.6; 302 2.1; 332 1.9; 365 0.4; 402 1.4; 442 1.9; 486 2.1; 535 2.2; 588 2.2; 647 2.0; 712 1.7; 783 1.3; 861 0.8; 947 0.2; 1042 -0.2; 1146 -0.3; 1261 0.2; 1387 -1.3; 1526 -2.2; 1678 -2.6; 1846 -2.7; 2031 -2.5; 2234 -2.2; 2457 -1.5; 2703 -1.0; 2973 5.9; 3270 0.8; 3597 1.2; 3957 3.2; 4353 3.8; 4788 5.2; 5267 -0.5; 5793 -11.0; 6373 -5.9; 7010 1.6; 7711 0.2; 8482 0.0; 9330 0.0; 10263 -1.0; 11289 -6.5; 12418 -11.2; 13660 -8.9; 15026 -3.1; 16529 -2.2; 18182 -2.9; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Adam SP-5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Adam SP-5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 30 Hz    |  0.64 | 6.5 dB   |
| Peaking | 4806 Hz  |  3.06 | 8.0 dB   |
| Peaking | 5843 Hz  |  5.45 | -16.9 dB |
| Peaking | 8712 Hz  |  1.06 | 4.1 dB   |
| Peaking | 12606 Hz |  2.05 | -13.4 dB |
| Peaking | 303 Hz   |  6.23 | 1.8 dB   |
| Peaking | 584 Hz   |  1.53 | 2.5 dB   |
| Peaking | 1969 Hz  |  1.51 | -3.3 dB  |
| Peaking | 2962 Hz  | 11.12 | 7.2 dB   |
| Peaking | 18474 Hz |  3.08 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Adam%20SP-5/Adam%20SP-5.png)