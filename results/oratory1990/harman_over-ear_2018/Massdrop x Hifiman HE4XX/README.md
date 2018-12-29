# Massdrop x Hifiman HE4XX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 5.1; 49 4.5; 54 3.8; 60 3.1; 66 2.6; 72 2.1; 79 1.6; 87 1.3; 96 1.1; 106 0.9; 116 0.8; 128 0.6; 141 0.4; 155 0.2; 170 0.2; 187 0.2; 206 0.2; 227 0.4; 249 0.2; 274 0.3; 302 0.6; 332 0.9; 365 1.0; 402 0.9; 442 0.7; 486 1.3; 535 2.1; 588 2.4; 647 2.2; 712 1.9; 783 1.3; 861 0.7; 947 0.1; 1042 -0.1; 1146 0.0; 1261 0.6; 1387 1.8; 1526 3.6; 1678 4.3; 1846 4.9; 2031 5.7; 2234 3.4; 2457 0.4; 2703 -1.8; 2973 -2.4; 3270 -1.8; 3597 -0.0; 3957 0.9; 4353 1.4; 4788 4.1; 5267 4.9; 5793 2.1; 6373 -1.5; 7010 -1.7; 7711 -3.0; 8482 -0.2; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.8; 18182 -6.3; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman HE4XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman HE4XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.72 | 6.6 dB  |
| Peaking | 618 Hz   | 1.57 | 3.0 dB  |
| Peaking | 1903 Hz  | 1.71 | 10.1 dB |
| Peaking | 2973 Hz  | 0.42 | -5.6 dB |
| Peaking | 4937 Hz  | 2.51 | 8.8 dB  |
| Peaking | 2895 Hz  | 3.53 | -3.3 dB |
| Peaking | 3116 Hz  | 1.76 | 2.2 dB  |
| Peaking | 7767 Hz  | 2.8  | -3.0 dB |
| Peaking | 8724 Hz  | 3.9  | 3.0 dB  |
| Peaking | 11088 Hz | 3.22 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20HE4XX/Massdrop%20x%20Hifiman%20HE4XX.png)