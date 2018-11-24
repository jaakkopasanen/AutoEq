# Beyerdynamic DT 1990 PRO

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.5dB
GraphicEQ: 21 -0.4; 23 -0.5; 25 -0.7; 28 -0.9; 31 -1.1; 34 -1.3; 37 -1.4; 41 -1.5; 45 -1.6; 49 -1.7; 54 -1.9; 60 -2.0; 66 -2.1; 72 -2.2; 79 -2.3; 87 -2.6; 96 -2.9; 106 -3.2; 116 -3.7; 128 -4.0; 141 -4.3; 155 -4.4; 170 -4.5; 187 -4.5; 206 -4.4; 227 -4.3; 249 -4.0; 274 -3.8; 302 -3.5; 332 -3.3; 365 -3.0; 402 -2.8; 442 -2.5; 486 -2.2; 535 -1.8; 588 -1.5; 647 -1.2; 712 -0.9; 783 -0.8; 861 -0.6; 947 -0.3; 1042 0.2; 1146 0.4; 1261 0.2; 1387 -0.3; 1526 -0.8; 1678 -1.2; 1846 -1.0; 2031 -0.6; 2234 0.1; 2457 0.2; 2703 0.3; 2973 0.6; 3270 0.7; 3597 0.7; 3957 0.4; 4353 0.3; 4788 -0.2; 5267 0.9; 5793 1.2; 6373 -2.2; 7010 -5.7; 7711 -8.7; 8482 -11.4; 9330 -10.3; 10263 -4.7; 11289 -0.3; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -2.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1990 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-14**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1990 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.81 | -1.0 dB  |
| Peaking | 175 Hz   | 0.66 | -4.3 dB  |
| Peaking | 403 Hz   | 1.39 | -1.1 dB  |
| Peaking | 5547 Hz  | 3.84 | 3.0 dB   |
| Peaking | 8511 Hz  | 2.77 | -12.7 dB |
| Peaking | 1156 Hz  | 3.89 | 0.9 dB   |
| Peaking | 1706 Hz  | 3.56 | -1.2 dB  |
| Peaking | 3194 Hz  | 2.43 | 1.0 dB   |
| Peaking | 9593 Hz  | 6.43 | -2.8 dB  |
| Peaking | 11461 Hz | 2.78 | 2.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beyerdynamic%20DT%201990%20PRO/Beyerdynamic%20DT%201990%20PRO.png)