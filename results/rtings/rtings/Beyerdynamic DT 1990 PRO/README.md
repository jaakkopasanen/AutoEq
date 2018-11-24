# Beyerdynamic DT 1990 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 21 -0.8; 23 -0.9; 25 -0.9; 28 -1.1; 31 -1.2; 34 -1.2; 37 -1.3; 41 -1.3; 45 -1.4; 49 -1.4; 54 -1.5; 60 -1.7; 66 -2.0; 72 -2.2; 79 -2.5; 87 -2.9; 96 -3.3; 106 -3.7; 116 -4.2; 128 -4.5; 141 -4.8; 155 -5.0; 170 -5.1; 187 -5.1; 206 -4.9; 227 -4.8; 249 -4.6; 274 -4.5; 302 -4.4; 332 -4.2; 365 -4.0; 402 -3.9; 442 -3.7; 486 -3.4; 535 -3.0; 588 -2.6; 647 -2.2; 712 -1.7; 783 -1.3; 861 -0.8; 947 -0.3; 1042 0.2; 1146 0.2; 1261 -0.0; 1387 -0.2; 1526 -0.5; 1678 -0.8; 1846 -1.1; 2031 -1.0; 2234 -0.4; 2457 -0.3; 2703 -0.3; 2973 -0.5; 3270 -1.2; 3597 -1.5; 3957 -0.8; 4353 0.3; 4788 -0.0; 5267 0.4; 5793 -0.2; 6373 -4.8; 7010 -8.2; 7711 -9.8; 8482 -11.8; 9330 -11.8; 10263 -8.1; 11289 -4.6; 12418 -3.1; 13660 -2.6; 15026 -2.1; 16529 -1.6; 18182 -2.6; 20000 -4.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1990 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-5**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1990 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.15 | -0.7 dB  |
| Peaking | 225 Hz   | 0.61 | -6.4 dB  |
| Peaking | 234 Hz   | 1.61 | 2.2 dB   |
| Peaking | 5414 Hz  | 2.78 | 4.8 dB   |
| Peaking | 8499 Hz  | 1.41 | -12.7 dB |
| Peaking | 1108 Hz  | 2.97 | 1.2 dB   |
| Peaking | 2102 Hz  | 2.24 | -1.3 dB  |
| Peaking | 2323 Hz  | 3.33 | 1.4 dB   |
| Peaking | 11847 Hz | 4.99 | 1.5 dB   |
| Peaking | 19873 Hz | 1.48 | -4.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Beyerdynamic%20DT%201990%20PRO/Beyerdynamic%20DT%201990%20PRO.png)