# Massdrop x Hifiman HE4XX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.7; 87 5.1; 96 4.4; 106 3.7; 116 3.1; 128 2.4; 141 1.8; 155 1.2; 170 0.8; 187 0.5; 206 0.3; 227 0.4; 249 0.2; 274 0.3; 302 0.6; 332 0.9; 365 1.0; 402 0.9; 442 0.7; 486 1.3; 535 2.1; 588 2.4; 647 2.2; 712 1.9; 783 1.3; 861 0.7; 947 0.1; 1042 -0.1; 1146 0.0; 1261 0.6; 1387 1.8; 1526 3.6; 1678 4.3; 1846 4.9; 2031 5.7; 2234 3.4; 2457 0.4; 2703 -1.8; 2973 -2.4; 3270 -1.8; 3597 -0.0; 3957 0.9; 4353 1.4; 4788 4.1; 5267 4.9; 5793 2.1; 6373 -1.5; 7010 -1.7; 7711 -3.0; 8482 -0.2; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.8; 18182 -6.3; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Hifiman HE4XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Hifiman HE4XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.46 | 6.8 dB  |
| Peaking | 635 Hz  | 1.83 | 3.2 dB  |
| Peaking | 1883 Hz | 1.61 | 10.5 dB |
| Peaking | 2825 Hz | 0.41 | -5.9 dB |
| Peaking | 4958 Hz | 2.53 | 8.8 dB  |
| Peaking | 18 Hz   | 2.1  | 1.2 dB  |
| Peaking | 2861 Hz | 5.46 | -1.3 dB |
| Peaking | 3715 Hz | 6.9  | 1.8 dB  |
| Peaking | 7622 Hz | 3.14 | -3.3 dB |
| Peaking | 8816 Hz | 2.19 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Hifiman%20HE4XX/Massdrop%20x%20Hifiman%20HE4XX.png)