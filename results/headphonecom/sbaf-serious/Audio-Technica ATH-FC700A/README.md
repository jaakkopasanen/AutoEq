# Audio-Technica ATH-FC700A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.3; 54 4.3; 60 4.5; 66 3.8; 72 2.7; 79 1.8; 87 1.1; 96 0.5; 106 -0.1; 116 -0.4; 128 -0.2; 141 0.8; 155 0.1; 170 -0.2; 187 -0.2; 206 -0.1; 227 -0.1; 249 -0.0; 274 -1.0; 302 -0.9; 332 -0.5; 365 -0.3; 402 -0.2; 442 0.0; 486 0.1; 535 0.3; 588 0.5; 647 0.6; 712 0.9; 783 0.7; 861 0.4; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -0.8; 1526 -1.7; 1678 -2.2; 1846 -2.8; 2031 -3.1; 2234 -2.9; 2457 -1.9; 2703 -0.6; 2973 0.5; 3270 1.6; 3597 2.3; 3957 2.9; 4353 3.2; 4788 3.7; 5267 5.7; 5793 -4.8; 6373 -5.0; 7010 -9.4; 7711 -7.4; 8482 -4.9; 9330 -1.9; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.6; 15026 -3.8; 16529 -3.8; 18182 -1.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-FC700A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-FC700A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.81 | 6.9 dB   |
| Peaking | 2035 Hz  | 2.19 | -3.8 dB  |
| Peaking | 4832 Hz  | 1.67 | 7.1 dB   |
| Peaking | 6927 Hz  | 2.41 | -11.8 dB |
| Peaking | 16472 Hz | 2.71 | -4.5 dB  |
| Peaking | 64 Hz    | 3.78 | 1.5 dB   |
| Peaking | 110 Hz   | 2.53 | -1.4 dB  |
| Peaking | 296 Hz   | 3.54 | -1.2 dB  |
| Peaking | 711 Hz   | 2.6  | 1.0 dB   |
| Peaking | 10622 Hz | 4.44 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio-Technica%20ATH-FC700A/Audio-Technica%20ATH-FC700A.png)